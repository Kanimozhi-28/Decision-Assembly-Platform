from typing import List, Dict, Optional
import json
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
import uuid
from qdrant_client import models
from app.db.database import get_pool

class AssembleService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_store = QdrantStore()

    def log(self, msg):
        # Keep file logging for production debugging if needed, or remove.
        # Removing print/file logging to be clean.
        pass

    async def assemble_experience(self, site_id: str, intent: str, context: Optional[Dict] = None):
        """
        SIMPLIFIED GRID ASSEMBLY
        Rule: Show ONLY visible products (max 4)
        No category detection, no RAG, no gap filling
        """
        try:
            result = await self._assemble_core(site_id, intent, context)
            # Ensure no None IDs
            result["products"] = [p for p in result["products"] if p.get("id") and p.get("url")]
            return result
        except Exception as e:
            import traceback
            error_msg = f"[ASSEMBLE ERROR]: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            from fastapi import HTTPException
            raise HTTPException(status_code=500, detail=f"Assembly Error: {str(e)}")

    async def _assemble_core(self, site_id: str, intent: str, context: Optional[Dict] = None):
        """
        RAG-BASED ASSEMBLY
        1. Embed the intent + context (e.g. page title)
        2. Semantic Search in Qdrant
        3. Retrieve relevant products
        4. Mix with currently viewed products if needed
        """
        try:
            context = context or {}
            # Products user is currently viewing/interacting with
            current_product_ids = context.get("product_ids", [])
            visible_product_urls = context.get("visible_product_urls", [])
            page_title = context.get("page_title", "")
            
            collection_name = "dap_products"
            products = []
            seen_urls = set()
    
            # 1. SECTION VISIBILITY LOCK (SL-001)
            # If visible products are provided, we MUST use ONLY those.
            if visible_product_urls:
                self.log(f"[ASSEMBLE] Enforcing Section Visibility Lock for {len(visible_product_urls)} products")
                
                # Strategy: Fetch all site products (limit 100) and filter in Python
                # This bypasses Qdrant URL filtering issues and is more efficient (1 query)
                try:
                    res = self.qdrant_store.client.scroll(
                        collection_name=collection_name,
                        scroll_filter=models.Filter(
                            must=[
                                models.FieldCondition(key="site_id", match=models.MatchValue(value=str(site_id)))
                            ]
                        ),
                        limit=200
                    )
                    site_products, _ = res
                    
                    # Create lookup map: URL -> Point
                    url_map = {}
                    for p in site_products:
                        payload = p.payload
                        if payload and payload.get("url"):
                            url_map[payload.get("url")] = p
                            # self.log(f"[ASSEMBLE] Loaded product URL: {payload.get('url')}")
                    
                    self.log(f"[ASSEMBLE] Loaded {len(url_map)} products from site {site_id}")
                    for u in list(url_map.keys())[:5]:
                        self.log(f"[ASSEMBLE] Example URL: {u}")
                            
                    for url in visible_product_urls:
                        # Generate variants
                        variants = [url]
                        if "localhost" in url:
                            variants.append(url.replace("localhost", "127.0.0.1"))
                        elif "127.0.0.1" in url:
                            variants.append(url.replace("127.0.0.1", "localhost"))
                            
                        # Check map
                        found_point = None
                        for v in variants:
                            if v in url_map:
                                found_point = url_map[v]
                                break
                        
                        if found_point:
                            if url in seen_urls:
                                continue
                            seen_urls.add(url)
                            
                            payload = found_point.payload
                            products.append({
                                "id": payload.get("product_id") or str(found_point.id),
                                "title": payload.get("title", "Untitled"),
                                "url": url,
                                "price": payload.get("price", "N/A"),
                                "description": payload.get("text", "")[:200],
                                "features": payload.get("features", []),
                                "category": payload.get("category", "general")
                            })
                        else:
                            # FALLBACK: Try matching by filename if path mismatch (e.g. urljoin bug)
                            filename = url.split('/')[-1]
                            if filename and not filename.endswith('.html'):
                                filename += '.html' # Heuristic
                                
                            for map_url, point in url_map.items():
                                if map_url.endswith(filename):
                                    if url in seen_urls:
                                        continue
                                    seen_urls.add(url)
                                    payload = point.payload
                                    products.append({
                                        "id": payload.get("product_id") or str(point.id),
                                        "title": payload.get("title", "Untitled"),
                                        "url": url,
                                        "price": payload.get("price", "N/A"),
                                        "description": payload.get("text", "")[:200],
                                        "features": payload.get("features", []),
                                        "category": payload.get("category", "general")
                                    })
                                    break

                    # Enforce Grid size = min(4, count)
                    products = products[:4]
                    
                except Exception as e:
                    self.log(f"[ASSEMBLE] Lock retrieval failed: {e}")
    
            # 2. RAG FALLBACK (Trigger if no products found yet, even if URLs were provided)
            # PRD §7.6.1: Strict Filtering for specific intents
            strict_intents = ["compare_options", "understand_differences"]
            
            if not products and intent not in strict_intents:
                detected_category = self._detect_category(context)
                if visible_product_urls:
                    print(f"[ASSEMBLE] Section Visibility Lock returned 0 products. Falling back to RAG for site_id: {site_id}, category: {detected_category}")
                else:
                    print(f"[ASSEMBLE] No visible products provided, falling back to RAG. Category: {detected_category}")
                
                # Improved RAG Query (PRD v1.2 Relevance Tuning)
                query_text = f"Show me {detected_category} products for {intent.replace('_', ' ')} based on {page_title}. {detected_category} {detected_category}"
                query_vector = await self.embedding_service.generate_embedding(query_text)
                
                try:
                    must_conditions = [
                        models.FieldCondition(key="site_id", match=models.MatchValue(value=str(site_id)))
                    ]
                    # Strict Category Scoping (Avoids cross-domain noise)
                    if detected_category != "general":
                        # If it's a specific Healthcare domain (cardiology, etc.) or Banking domain
                        must_conditions.append(
                            models.FieldCondition(key="category", match=models.MatchValue(value=detected_category))
                        )

                    query_filter = models.Filter(must=must_conditions)
                    search_results = self.qdrant_store.search(
                        collection_name=collection_name,
                        vector=query_vector,
                        limit=10,
                        query_filter=query_filter
                    )
                    
                    for p in search_results:
                        payload = p.payload
                        url = payload.get("url")
                        if url in seen_urls: continue
                        seen_urls.add(url)
                        
                        products.append({
                            "id": payload.get("product_id") or url,
                            "title": payload.get("title", "Untitled"),
                            "url": url,
                            "price": payload.get("price", "N/A"),
                            "description": payload.get("text", "")[:200],
                            "features": payload.get("features", []),
                            "category": payload.get("category", "general")
                        })
                        if len(products) >= 4: break
                except Exception as e:
                    print(f"[ASSEMBLE] Fallback search error: {e}")
            elif not products and intent in strict_intents:
                print(f"[ASSEMBLE] Strict intent '{intent}' returned 0 products. Skipping RAG fallback.")
    
            # 3. Common Processing (Rationale & Blocks)
            # 4. Generate rationales
            try:
                rationales = await self._generate_rationales(products, intent, site_id)
            except Exception as e:
                print(f"[ASSEMBLE] Rationale generation error: {e}")
                rationales = {p.get("id", p.get("url")): f"Consider {p.get('title')}" for p in products}
            
            # 5. Intent -> Block Mapping (PRD §7.6)
            final_block_mapping = {}
            try:
                pool = await get_pool()
                async with pool.acquire() as conn:
                    config = await conn.fetchrow(
                        "SELECT block_mapping FROM dap.site_config WHERE site_id = $1",
                        uuid.UUID(str(site_id))
                    )
                    if config and config["block_mapping"]:
                        db_mapping = config["block_mapping"]
                        if isinstance(db_mapping, str):
                            final_block_mapping = json.loads(db_mapping)
                        else:
                            final_block_mapping = db_mapping
            except Exception as e:
                print(f"[ASSEMBLE] Block mapping fetch error: {e}")
    
            # Fallback to defaults
            if not final_block_mapping:
                final_block_mapping = {
                    "help_me_choose": ["shortlist", "recommendation", "trade-off", "action"],
                    "compare_options": ["comparison", "costs", "benefits", "limitations"],
                    "check_eligibility": ["eligibility", "use-case-fit", "action"],
                    "understand_differences": ["comparison", "trade-off", "examples"],
                    "just_exploring": ["shortlist", "benefits", "custom-query"]
                }
            
            block_types = final_block_mapping.get(intent, ["shortlist"])
            blocks = []
            for bt in block_types:
                block_products = []
                message = ""
                
                if bt == "shortlist":
                    block_products = products[:4]
                    message = "Based on your current section, here are the top matching plans."
                elif bt == "recommendation":
                    block_products = products[:1]
                    message = f"Our top pick for your {intent.replace('_', ' ')} needs."
                elif bt == "trade-off":
                    block_products = products[:2]
                    message = "Comparing the key differences between these two options."
                elif bt == "comparison":
                    block_products = products[:4]
                    message = "Feature-by-feature comparison of our available plans."
                elif bt == "action":
                    block_products = products[:1]
                    message = "Ready to proceed? This plan offers the best balance for you."
                else:
                    block_products = products[:2]
                    message = f"Insights on {bt.replace('-', ' ')}."

                if block_products or bt in ["shortlist", "comparison", "recommendation", "trade-off"]:
                    blocks.append({
                        "type": bt,
                        "products": block_products,
                        "message": message
                    })
    
            return {
                "blocks": blocks,
                "products": products,
                "rationales": rationales,
                "intent": intent,
                "message": f"Found {len(products)} relevant options."
            }
                
        except Exception as e:
            print(f"[ASSEMBLE] Error in RAG: {e}")
            import traceback
            traceback.print_exc()
            return {
                "error": str(e),
                "products": [],
                "blocks": [],
                "message": f"Error during assembly: {str(e)}"
            }

    async def _generate_rationales(self, products: List[Dict], intent: str, site_id: str) -> Dict[str, str]:
        """
        Generate intent-based rationales for each product.
        Attempts to fetch from DB first, then falls back to internal templates.
        """
        rationales = {}
        template_text = None
        
        # 1. Try to fetch from Database
        try:
            pool = await get_pool()
            async with pool.acquire() as conn:
                row = await conn.fetchrow(
                    "SELECT template_text FROM dap.rationale_templates WHERE site_id = $1 AND intent = $2",
                    uuid.UUID(str(site_id)),
                    intent
                )
                if row:
                    template_text = row["template_text"]
                    print(f"[ASSEMBLE] Using DB template for intent: {intent}")
        except Exception as e:
            print(f"[ASSEMBLE] DB Template fetch error: {e}")

        # 2. Fallback to code-based templates if DB fails or is empty
        if not template_text:
            internal_templates = {
                "help_me_choose": "{title} is a top choice due to its competitive {price} and strong ratings in this category.",
                "compare_options": "Compare {title} against others; it stands out for its specific features and {price} point.",
                "check_eligibility": "Looking at {title}, it fits the profile for users seeking reliable {price} solutions.",
                "just_exploring": "{title} is worth considering while exploring options, offering solid {price} and features.",
                "best_value": "{title} offers the best balance of features and {price} for most users.",
                "most_popular": "{title} is a widely chosen option among users looking for efficiency and value."
            }
            template_text = internal_templates.get(intent, "Consider {title} ({price}) - Based on your recent activity and section context.")
            print(f"[ASSEMBLE] Using internal template for intent: {intent}")

        # 3. Apply formatting (Handling both {curly} and {{handlebar}} styles)
        for product in products:
            res = template_text
            
            # Key mappings for DB templates ({{product_name}}, {{price}}, {{intent}})
            res = res.replace("{{product_name}}", product.get("title", "this product"))
            res = res.replace("{{price}}", product.get("price", "N/A"))
            res = res.replace("{{intent}}", intent.replace("_", " "))
            
            # Python-style formatting for internal and some DB templates
            # Use safe replace instead of .format() to avoid KeyError with unknown curly braces
            title = product.get("title", "this product")
            description = product.get("description", "")[:100]
            
            res = res.replace("{title}", title)
            res = res.replace("{description}", description)
                
            rationales[product.get("id", product.get("url"))] = res
        
        return rationales

    def _detect_category(self, context: Dict) -> str:
        """
        Detect category from page title, URL or context.
        """
        title = context.get("page_title", "").lower()
        url = context.get("url", "").lower()
        
        # Mapping rules based on keywords (expanded for Healthcare and Banking)
        mappings = {
            "savings": ["saving", "deposit", "interest", "account"],
            "loans": ["loan", "mortgage", "borrow", "lending"],
            "cards": ["card", "credit card", "visa", "mastercard"],
            "insurance": ["insurance", "guard", "protection", "shield"],
            "mobiles": ["phone", "mobile", "smartphone", "iphone", "pixel", "galaxy"],
            "laptops": ["laptop", "notebook", "macbook", "ultrabook"],
            "appliances": ["appliance", "hub", "kitchen", "fridge", "washer", "oven"],
            "cardiology": ["cardiology", "heart", "cardiac", "angioplasty", "bypass", "ecg"],
            "neurology": ["neurology", "brain", "stroke", "neuro"],
            "pediatrics": ["pediatrics", "child", "newborn", "baby", "vaccination"],
            "orthopedics": ["orthopedics", "joint", "knee", "hip", "bone"],
            "diagnostics": ["diagnostic", "mri", "scan", "checkup", "test", "screening"]
        }
        
        for cat, keywords in mappings.items():
            if any(k in title for k in keywords) or any(k in url for k in keywords):
                return cat
                
        # General healthcare fallback if no specific domain matched
        healthcare_keywords = ["health", "medical", "doctor", "hospital", "clinic"]
        if any(k in title for k in healthcare_keywords) or any(k in url for k in healthcare_keywords):
            return "healthcare"
            
        return "general"
