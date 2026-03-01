import asyncio
import asyncpg
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
from pydantic import BaseModel
from typing import List, Optional, Dict
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import requests

load_dotenv()

app = FastAPI(title="DAP Backend API")

# Configuration
print("DAP Backend VERSION: 3.0 (Multi-Site Ready)")
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral:7b-instruct")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
DATABASE_URL = os.getenv("DATABASE_URL")

# Global DB Pool
db_pool = None
RESPONSE_CACHE = {}
PENDING_REQUESTS = {}

@app.on_event("startup")
async def startup():
    global db_pool
    try:
        db_pool = await asyncpg.create_pool(DATABASE_URL)
        print("Connected to PostgreSQL Database Pool")
    except Exception as e:
        print(f"❌ Database Connection Error: {e}")

@app.on_event("shutdown")
async def shutdown():
    if db_pool:
        await db_pool.close()

# Create static directory if it doesn't exist
os.makedirs("backend/static", exist_ok=True)

# Mount static files to serve the SDK
app.mount("/sdk", StaticFiles(directory="backend/static"), name="sdk")

# Enable CORS for frontend and SDK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Keep as fallback, endpoint validation handles it
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def validate_origin(request: Request, site_id: str):
    """Business logic for origin validation"""
    origin = request.headers.get("origin")
    if not origin: return # Internal or local request without origin
    
    # 🧪 DEVELOPMENT OVERRIDE: Allow common testing origins
    testing_origins = ["http://127.0.0.1:5500", "http://localhost:5500", "http://localhost:5173", "http://127.0.0.1:5173"]
    if origin in testing_origins:
        return # Unblocked for local testing
        
    # Handle non-UUID site IDs (like 'testing-website' slugs)
    # If the user uses a slug, we try to find it in the 'name' column
    try:
        # Check if it's a valid UUID
        import uuid
        uuid.UUID(site_id)
        where_clause = "site_id = $1::uuid"
    except (ValueError, TypeError):
        # Fallback to name/slug lookup if site_id is a string like 'testing-website'
        where_clause = "name ILIKE $1 OR domain ILIKE $1"

    async with db_pool.acquire() as conn:
        allowed = await conn.fetchval(f"SELECT allowed_origins FROM sites WHERE {where_clause}", site_id)
        if allowed:
            origins_list = json.loads(allowed)
            if origin not in origins_list:
                print(f"🛑 SECURITY VOILATION: Origin {origin} not allowed for site {site_id}")
                raise HTTPException(status_code=403, detail="Origin not authorized")

# Models
class IntentSubmission(BaseModel):
    site_id: str
    user_id: str
    intent_id: str
    context_url: str

class Interaction(BaseModel):
    site_id: str
    user_id: str
    event_type: str
    metadata: Dict

class BehaviorLog(BaseModel):
    site_id: str
    type: str       # e.g., 'hover', 'scroll', 'click', 'select'
    metadata: str   # e.g., text content of the hovered element, scroll percentage
    url: str        # current page URL
    history: List[str] # List of previously visited product URLs
    dwell_time: float # Time spent on current page in seconds

class AssemblyContext(BaseModel):
    url: str
    page_title: str
    product_ids: List[str]

class AssemblyRequest(BaseModel):
    site_id: str
    intent_id: str
    context: AssemblyContext

class BlockRequest(BaseModel):
    site_id: str
    block_id: str
    product_ids: List[str]

# Endpoints

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/config/{site_id}")
async def get_config(request: Request, site_id: str):
    """Return site-specific configuration from PostgreSQL"""
    await validate_origin(request, site_id)
    if not db_pool:
        raise HTTPException(status_code=500, detail="Database not connected")
    
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow("""
            SELECT s.name as site_name, sc.branding, sc.triggers, sc.intents, sc.intent_map, sc.commentary_templates
            FROM site_config sc
            JOIN sites s ON s.site_id = sc.site_id
            WHERE sc.site_id = $1::uuid
        """, site_id)
        
        if not row:
            # Global Fallback
            return {
                "site_id": site_id,
                "name": "Assistant",
                "branding": {"primaryColor": "#0a1628", "accentColor": "#d4af37"},
                "triggers": {"multipleProductViews": {"threshold": 3}, "sessionHesitation": {"dwellTime": 45}},
                "intents": [
                    {"id": "compare", "label": "Compare options"},
                    {"id": "help_choose", "label": "Help me choose"},
                    {"id": "exploring", "label": "Just exploring"}
                ]
            }
        
        return {
            "site_id": site_id,
            "name": row['site_name'],
            "branding": json.loads(row['branding']),
            "triggers": json.loads(row['triggers']),
            "intents": json.loads(row['intents']),
            "intent_map": json.loads(row['intent_map'] or '{}'),
            "commentary_templates": json.loads(row['commentary_templates'] or '{}')
        }

@app.post("/intent")
async def submit_intent(request: Request, submission: IntentSubmission):
    """Record user intent and return confirmation"""
    await validate_origin(request, submission.site_id)
    print(f"Intent received: {submission.intent_id} from {submission.user_id}")
    return {"status": "success", "message": "Intent recorded"}

@app.post("/assemble")
async def assemble_grid(request: Request, req: AssemblyRequest):
    """Assemble the decision grid based on intent and history using RAG"""
    await validate_origin(request, str(req.site_id))
    print(f"Assembling grid for intent: {req.intent_id} on {req.context.url}")
    
    # Init Clients
    client = AsyncOpenAI(base_url=OLLAMA_URL, api_key="ollama")
    qdrant = QdrantClient(url=QDRANT_URL)
    
    # 1. Fetch Dynamic Configuration for Site
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow("""
            SELECT s.name, sc.intent_map FROM sites s 
            JOIN site_config sc ON s.site_id = sc.site_id 
            WHERE s.site_id = $1::uuid
        """, req.site_id)
        
        # AGNOSTICISM: Collection names are now site-derived
        collection_name = f"dap_{str(req.site_id).replace('-', '_')}"
    
    # 2. Determine Scope (Dynamic Category Inference)
    # Strategy: Derive category from URL segments, or fall back to product history if on a landing page
    path_segments = [s for s in req.context.url.split('/') if s and s not in ['http:', 'https:', 'localhost:5173', 'localhost:5174', '127.0.0.1:5173', '127.0.0.1:5174']]
    active_category = "general"
    
    # REFINEMENT: Robust category detection
    if path_segments:
        # Check if the first segment is a known category in Qdrant
        potential_cat = path_segments[0]
        # Skip generic segments
        if potential_cat not in ["products", "solutions", "offerings", "home"]:
            active_category = potential_cat
    
    # If on a generic landing page, infer category from viewed products
    landing_pages = ["general", "financing-solutions", "banking", "home", ""]
    if active_category in landing_pages and req.context.product_ids:
        # Check folders in product history (e.g. /loans/home -> loans)
        categories = []
        for pid in req.context.product_ids:
            if not pid: continue
            parts = [p for p in pid.split('/') if p and p not in ['http:', 'https:', 'localhost:5173', 'localhost:5174', '127.0.0.1:5173', '127.0.0.1:5174']]
            if parts: categories.append(parts[0])
            
        if categories:
            # Most common category wins
            from collections import Counter
            active_category = Counter(categories).most_common(1)[0][0]
            print(f"INFERRED CATEGORY: {active_category} from history")

    filter_product_ids = [pid for pid in req.context.product_ids if pid]
    
    # STRICT FILTERING for Compare intent: Only include products from the same category
    if req.intent_id in ["compare", "understand_differences"]:
        original_count = len(filter_product_ids)
        new_list = []
        for pid in filter_product_ids:
            # 1. Must match active category
            if not (f"/{active_category}/" in pid or pid.endswith(f"/{active_category}")):
                continue
            
            # 2. ARCHITECTURE FIX: Must have at least 2 segments (item level)
            # e.g. /loans/home is kept, but /loans is dumped.
            path_parts = [p for p in pid.split('/') if p and p not in ['http:', 'https:', 'localhost:5173', 'localhost:5174', '127.0.0.1:5173', '127.0.0.1:5174']]
            if len(path_parts) >= 2:
                new_list.append(pid)
        
        # RECENCY FILTER: Only use the last 4 unique relevant products
        # This prevents "leakage" from old comparisons (e.g. an old Home Loan)
        # while keeping the current journey (e.g. Auto/Personal) fresh.
        filter_product_ids = new_list[-4:]
        if len(new_list) > 4:
            print(f"RECENCY FILTER: Focused on 4 most recent products (Purged {len(new_list) - 4} stale items)")
        else:
            filter_product_ids = new_list
        
        if len(filter_product_ids) < original_count:
            print(f"STRICT SCOPING: Filtered out {original_count - len(filter_product_ids)} non-product or stale URLs.")

    
    # 3. Get Embedding
    # 3. Get Embedding
    # PRD REQUIREMENT: Generate embedding for context execution
    # TIMEOUT SAFEGUARD: If remote embedding fails/times out, we proceed with zero-vector
    # because 'compare' intent uses exact URL matching anyway.
    embedding = None
    query_text = f"{req.intent_id} {active_category} {req.context.page_title}"
    ollama_api = OLLAMA_URL.replace("/v1", "/api/embeddings")
    
    print(f"GENERATING EMBEDDING for '{req.intent_id}'...")
    try:
        # Use a reasonable timeout (e.g. 10s). If it fails, we don't block the UI forever.
        resp = requests.post(ollama_api, json={"model": "nomic-embed-text", "prompt": query_text}, timeout=10)
        if resp.status_code == 200:
            embedding = resp.json().get("embedding")
            print("Embedding generated successfully")
        else:
            print(f"Embedding failed: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"Embedding timed out or error (proceeding with fallback): {e}")

    # 4. Search Qdrant with Dynamic Filtering
    try:
        from qdrant_client.http import models
        must_conditions = []
        # Dynamic exclusion: Exclude current page from results EXCEPT for comparisons
        must_not_conditions = []
        if req.intent_id not in ["compare", "understand_differences"]:
            must_not_conditions.append(
                models.FieldCondition(key="url", match=models.MatchValue(value=req.context.url))
            )

        if req.intent_id == "compare" or req.intent_id == "understand_differences":
            if not filter_product_ids:
                return {
                    "status": "partial",
                    "items": [],
                    "blocks": ["Shortlist"],
                    "message": "View a few more products to see a side-by-side comparison."
                }
            
            # STRICT FILTER: Only show what the user saw in this specific category
            must_conditions.append(
                models.FieldCondition(key="url", match=models.MatchAny(any=filter_product_ids))
            )
            # Cap comparison to a readable number (max 4)
            search_limit = min(len(filter_product_ids), 4)
        else:
            # For discovery intents, limit to 3 recommendations in the same category
            search_limit = 3
            if active_category != "general":
                must_conditions.append(
                    models.FieldCondition(key="category", match=models.MatchValue(value=active_category))
                )

        query_filter = models.Filter(must=must_conditions if must_conditions else None, must_not=must_not_conditions)

        # For Compare intent, don't use score threshold since we're doing exact URL matching
        # For discovery intents, use threshold to ensure relevance
        use_score_threshold = (req.intent_id not in ["compare", "understand_differences"]) and embedding

        search_results = qdrant.search(
            collection_name=collection_name,
            query_vector=embedding if embedding else [0.0]*768,
            query_filter=query_filter,
            limit=search_limit,
            score_threshold=0.25 if use_score_threshold else None
        )

        # ARCHITECTURE: Discovery Fallback (PRD §5.5)
        # If category-specific discovery returns 0, try site-wide
        if not search_results and req.intent_id not in ["compare", "understand_differences"]:
            print(f"DISCOVERY FALLBACK: Retrying search for {active_category} without category filter...")
            fallback_filter = models.Filter(must_not=must_not_conditions)
            search_results = qdrant.search(
                collection_name=collection_name,
                query_vector=embedding if embedding else [0.0]*768,
                query_filter=fallback_filter,
                limit=search_limit,
                score_threshold=None # Remove threshold for fallback to guarantee recommendations
            )

        
        # 5. Format and Parallel Rationale Generation
        # 5. Format and Template-Based Rationale Generation
        async def generate_rationale(item):
            # ARCHITECTURE: Retrieve template from rationale_templates table (TAD §8.3)
            async with db_pool.acquire() as conn:
                template = await conn.fetchval("""
                    SELECT template_text FROM rationale_templates 
                    WHERE site_id = $1::uuid AND category = $2 
                    ORDER BY RANDOM() LIMIT 1
                """, req.site_id, active_category)
                
                if not template:
                    # Fallback to general template
                    template = await conn.fetchval("""
                        SELECT template_text FROM rationale_templates 
                        WHERE site_id = $1::uuid AND (category IS NULL OR category = 'general')
                        ORDER BY RANDOM() LIMIT 1
                    """, req.site_id)

            if template:
                # Basic context injection
                return template.replace("{title}", item['title']).replace("{intent}", req.intent_id.replace('_', ' '))
            
            # Final hardcoded fallback
            return f"Strategic fit for your {req.intent_id.replace('_', ' ')} journey."

        raw_items = []
        for result in search_results:
            p = result.payload
            raw_items.append({
                "id": p.get("url"),
                "title": p.get("title", "Product"),
                "description": p.get("content_preview", ""),
                "url": p.get("url")
            })

        # SNAPPY UX: Parallel execution of DB lookups
        rationale_tasks = [generate_rationale(item) for item in raw_items]
        rationales = await asyncio.gather(*rationale_tasks)

        items = []
        for i, item in enumerate(raw_items):
            items.append({
                "id": item["id"],
                "title": item["title"],
                "description": item["description"],
                "url": item["url"],
                "rationale": rationales[i]
            })
            
        # 6. Intent -> Blocks (DE-HARDCODED: Fetch from site_config)
        db_intent_map = json.loads(row['intent_map'] or '{}') if row else {}
        category_map = db_intent_map.get(active_category, db_intent_map.get('default', {}))
        blocks = category_map.get(req.intent_id, ["Shortlist", "Recommendations"])

        return {
            "status": "success",
            "intent": req.intent_id,
            "items": items,
            "blocks": blocks,
            "category": active_category
        }
    except Exception as e:
        print(f"❌ Assembly Error: {e}")
        return {"items": [], "blocks": ["Shortlist"], "error": str(e)}

@app.post("/analytics/track")
async def track_interaction(request: Request, interaction: Interaction):
    await validate_origin(request, interaction.site_id)
    return {"status": "ok"}

@app.post("/behavior/analyze")
async def analyze_behavior(request: Request, log: BehaviorLog):
    """Analyze behavior using Template Engine (Primary) and LLM (Secondary/Discovery)"""
    await validate_origin(request, log.site_id)
    
    if not db_pool:
        return {"commentary": "Assistant: Monitoring session..."}

    async with db_pool.acquire() as conn:
        # Fetch templates and branding
        row = await conn.fetchrow("""
            SELECT sc.commentary_templates, s.name 
            FROM site_config sc 
            JOIN sites s ON s.site_id = sc.site_id 
            WHERE sc.site_id = $1::uuid
        """, log.site_id)
        
        site_name = row['name'] if row else "Assistant"
        templates = json.loads(row['commentary_templates'] or '{}') if row else {}

    # TEMPLATE ENGINE (TAD §8.4 Alignment)
    # Fast, cost-effective, and low latency
    commentary = None
    
    if log.type == "hover" and log.dwell_time > 5:
        commentary = templates.get("cta_hover", "").replace("{item}", log.metadata)
    elif len(log.history) >= 2 and log.type != "hover":
        commentary = templates.get("multi_view", "").replace("{n}", str(len(log.history)))
    elif log.dwell_time > 45:
        commentary = templates.get("hesitation", "")
    
    if commentary:
        return {"commentary": f"{site_name}: {commentary}"}

    # FALLBACK/CACHING for LLM (if templates don't cover the event)
    cache_key = f"{log.type}:{log.metadata}:v3"
    if cache_key in RESPONSE_CACHE:
        return {"commentary": RESPONSE_CACHE[cache_key]}

    # Only use LLM for complex interactions or as a "Discovery" mechanism (v1.5 goal)
    # For now, we return the 'welcome' template as the stable base.
    welcome = templates.get("welcome", "Monitoring session for personalized insights.")
    return {"commentary": f"{site_name}: {welcome}"}



@app.post("/block-content")
async def get_block_content(request: Request, req: BlockRequest):
    """Generate contextual content for a specific grid block"""
    await validate_origin(request, req.site_id)
    
    if not req.product_ids:
        return {"content": "No products selected for analysis."}

    try:
        qdrant = QdrantClient(url=QDRANT_URL)
        collection_name = f"dap_{str(req.site_id).replace('-', '_')}"
        
        from qdrant_client import models
        points = qdrant.scroll(
            collection_name=collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(key="url", match=models.MatchAny(any=req.product_ids))
                ]
            ),
            limit=10,
            with_payload=True,
            with_vectors=False
        )[0]
        
        if not points:
            return {"content": "Could not find detailed information for these products."}
            
        context_data = []
        for p in points:
            payload = p.payload
            context_data.append(f"Product: {payload.get('title')}\nContent: {payload.get('content_preview')}")
            
        combined_context = "\n---\n".join(context_data)
        
        client = AsyncOpenAI(base_url=OLLAMA_URL, api_key="ollama")
        
        prompt = f"""
        Draft high-value content for the decision grid block: '{req.block_id}'
        
        Context (Product Details):
        {combined_context}
        
        Instructions:
        - If the block is 'Loan Comparison Matrix', provide a concise bulleted comparison of rates and terms.
        - If the block is 'Eligibility Checklist', list specific requirements found.
        - If the block is 'Personalized EMI Breakdown', explain general payment factors or estimate based on data.
        - If the block is 'Feature Comparison', highlight key technical or functional differences.
        - If the block is 'Rewards & Benefits', focus on cashback, points, or perks.
        - If the block is 'Fees & APR', provide a breakdown of costs.
        - Keep it concise, professional, and data-driven.
        - Do NOT include the block title '{req.block_id}' as a heading in your response.
        - Do NOT use placeholders.
        """
        
        response = await client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": "You are a professional financial assistant helping a user make a decision based on product data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=300
        )
        
        content = response.choices[0].message.content.strip()
        return {"content": content}
        
    except Exception as e:
        print(f"❌ Block Content Error: {e}")
        return {"content": f"Error generating content: {str(e)}"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
