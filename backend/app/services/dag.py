import asyncio
import json
import uuid
import os
from typing import TypedDict, Annotated, List

from app.db.database import get_pool
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore

# --- Define Graph State ---
class DagState(TypedDict):
    url: str
    site_id: str
    markdown: str
    config: dict
    error: str

class UniversalDAG:
    def __init__(self):
        from app.config import Settings
        settings = Settings()
        self.embeddings = EmbeddingService()
        self.qdrant = QdrantStore()
        
        # Initialize Provider
        from openai import AsyncOpenAI
        if settings.ollama_base_url:
            self.llm = AsyncOpenAI(
                api_key="ollama",
                base_url=settings.ollama_base_url
            )
            self.model_name = settings.ollama_model
        elif settings.perplexity_api_key:
            self.llm = AsyncOpenAI(
                api_key=settings.perplexity_api_key,
                base_url="https://api.perplexity.ai"
            )
            self.model_name = "sonar"
        else:
            self.llm = AsyncOpenAI(
                api_key=settings.openai_api_key,
                base_url=settings.llm_base_url
            )
            self.model_name = "gpt-4o-mini"
            
        self.graph = self._build_graph()

    def _build_graph(self):
        """
        Builds the LangGraph for site discovery.
        """
        from langgraph.graph import StateGraph, END
        workflow = StateGraph(DagState)

        # Define Nodes
        workflow.add_node("crawl", self.node_crawl)
        workflow.add_node("analyze", self.node_analyze)
        workflow.add_node("save", self.node_save)

        # Define Edges
        workflow.set_entry_point("crawl")
        workflow.add_edge("crawl", "analyze")
        workflow.add_edge("analyze", "save")
        workflow.add_edge("save", END)

        return workflow.compile()

    # --- Nodes ---

    async def node_crawl(self, state: DagState):
        """
        Node 1: Crawl the URL using Crawl4AI to get clean Markdown.
        """
        from crawl4ai import AsyncWebCrawler
        print(f"[DAG] Crawling {state['url']}...")
        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=state['url'])
                
                if not result.success:
                    return {"error": f"Crawl failed: {result.error_message}"}
                
                return {"markdown": result.markdown}
        except Exception as e:
            return {"error": str(e)}

    async def node_analyze(self, state: DagState):
        """
        Node 2: Use LLM to analyze markdown and extract selectors AND generate rationale templates.
        """
        if state.get("error"):
            return None # Stop processing

        print(f"[DAG] Analyzing content for {state['url']}...")
        
        prompt = f"""
        You are an expert web scraper and UX copywriter. Analyze the following markdown content from a website homepage.
        
        Task 1: Identify the CSS selectors or URL patterns for:
        1. Product Pages (regex pattern for URLs). Note: If the site uses flat HTML files, look for patterns like "product-" or "item-".
        2. "Add to Cart" or "Buy Now" buttons (CSS selector)
        3. Product Price (CSS selector)

        Task 2: Generate 3 distinct "Shopping Intents" that a user might have on this specific site (e.g., "Find cheapest", "Best for gaming", "Low interest rate").
        For each intent, write a short "Rationale Template" (1-2 sentences) explaining why a product matches that intent. Use {{product_name}} and {{price}} as placeholders.

        Return ONLY a raw JSON object (no markdown formatting) with this structure:
        {{
            "product_page_rules": ["product-", "/product/", "/p/"],
            "cta_selectors": [".selector1", "#selector1"],
            "price_selector": ".selector",
            "rationales": [
                {{ "intent": "intent_key_1", "label": "Human Readable Label 1", "template": "This {{product_name}} is a great choice because..." }},
                {{ "intent": "intent_key_2", "label": "Human Readable Label 2", "template": "At {{price}}, this offers..." }}
            ]
        }}

        MARKDOWN CONTENT:
        {state['markdown'][:4000]}  # Truncate to avoid token limits
        """

        try:
            response = await self.llm.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"} if "sonar" not in self.model_name and "llama" not in self.model_name.lower() else None
            )
            content = response.choices[0].message.content
            # Clean for local models
            content = content.replace("```json", "").replace("```", "").strip()
            
            config = json.loads(content)
            return {"config": config}
        except Exception as e:
            print(f"[DAG] LLM Error: {e}")
            fallback = {
                "product_page_rules": ["product-", "product_", "service-", "item-", "loan", "card", "saving", "/p/", "/product/"],
                "cta_selectors": ["button", ".btn", ".cta", "a.button"],
                "price_selector": ".price, .amount, .cost, .interest-rate",
                "rationales": [
                     { "intent": "help_me_choose", "label": "Help Me Choose", "template": "This {{product_name}} is a strong contender." },
                     { "intent": "compare_options", "label": "Compare Options", "template": "Compare {{product_name}} priced at {{price}}." },
                     { "intent": "check_eligibility", "label": "Check Eligibility", "template": "See if {{product_name}} fits your criteria." },
                     { "intent": "just_exploring", "label": "Just Exploring", "template": "Discover why {{product_name}} is popular." }
                ]
            }
            return {"config": fallback}

    async def node_save(self, state: DagState):
        """
        Node 3: Save the discovered config AND rationales to PostgreSQL.
        """
        if state.get("error") or not state.get("config"):
            return None

        print(f"[DAG] Saving config for {state['site_id']}...")
        config = state['config']
        
        try:
            pool = await get_pool()
            async with pool.acquire() as conn:
                # 1. Update Site Config
                await conn.execute(
                    """
                    UPDATE dap.site_config 
                    SET product_page_rules = $2, cta_selectors = $3, updated_at = now()
                    WHERE site_id = $1
                    """,
                    uuid.UUID(state['site_id']), 
                    json.dumps(config.get("product_page_rules", [])),
                    json.dumps(config.get("cta_selectors", []))
                )

                # 2. Update Rationales (Delete old, insert new)
                await conn.execute("DELETE FROM dap.rationale_templates WHERE site_id = $1", uuid.UUID(state['site_id']))
                
                rationales = config.get("rationales", [])
                if rationales:
                    records = [(uuid.UUID(state['site_id']), r["intent"], r["template"]) for r in rationales]
                    await conn.executemany(
                        """
                        INSERT INTO dap.rationale_templates (site_id, intent, template_text)
                        VALUES ($1, $2, $3)
                        """,
                        records
                    )

            print(f"[DAG] Config and Rationales saved successfully!")
            return {"site_id": state['site_id']}
        except Exception as e:
            print(f"[DAG] DB Error: {e}")
            return {"error": str(e)}

    # --- Public Methods ---

    async def run_discovery(self, url: str, site_id: str):
        """
        Trigger the LangGraph workflow.
        """
        initial_state = {"url": url, "site_id": site_id, "markdown": "", "config": {}, "error": ""}
        result = await self.graph.ainvoke(initial_state)
        return result

    async def sync_catalog(self, site_id: str, base_url: str):
        """
        Phase 2: Crawl the catalog based on discovered rules.
        """
        from crawl4ai import AsyncWebCrawler
        print(f"[DAG] Starting Catalog Sync for {site_id}...")
        
        # 1. Fetch Rules from DB
        pool = await get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow("SELECT product_page_rules, cta_selectors, price_selector FROM dap.site_config WHERE site_id = $1", uuid.UUID(site_id))
            if not row:
                print(f"[DAG] No config found for {site_id}. Run discovery first.")
                return

            rules = json.loads(row['product_page_rules']) if row['product_page_rules'] else []
            cta_selectors = json.loads(row['cta_selectors']) if row['cta_selectors'] else []
            price_selector = row['price_selector']

        if not rules:
            print("[DAG] No product page rules found.")
            return

        # 2. Crawl Homepage to find Product Links
        print(f"[DAG] Scanning homepage {base_url} for product links matching {rules}...")
        product_links = set()
        
        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=base_url)
                if result.success:
                    print(f"[DAG] Found {len(result.links)} structured links. Total links might be higher in markdown.")
                    
                    # 1. Start with structured links
                    raw_links = []
                    if isinstance(result.links, dict):
                        for group in result.links.values():
                            raw_links.extend([l.get('href', str(l)) if isinstance(l, dict) else str(l) for l in group])
                    else:
                        raw_links = [l.get('href', str(l)) if isinstance(l, dict) else str(l) for l in result.links] if result.links else []

                    # 2. Add Regex extraction from markdown as fallback/supplement
                    import re
                    # Look for [text](url)
                    md_links = re.findall(r'\[.*?\]\((.*?)\)', result.markdown)
                    raw_links.extend(md_links)

                    # Deduplicate
                    raw_links = list(set(raw_links))
                    print(f"[DAG] Total unique links after regex: {len(raw_links)}")

                    for href in raw_links:
                        # DEBUG PRINT
                        matches = [rule for rule in rules if rule in href]
                        if matches:
                            print(f"[DAG] Link Match: {href} matched rules {matches}")
                            # Normalize URL
                            from urllib.parse import urljoin
                            full_base = base_url if base_url.endswith('/') else f"{base_url}/"
                            href = urljoin(full_base, href)
                            product_links.add(href)
                        else:
                            # print(f"[DAG] No Match: {href}")
                            pass
        except Exception as e:
            print(f"[DAG] Homepage crawl failed: {e}")
            return

        print(f"[DAG] Found {len(product_links)} product pages to scrape.")
        
        # 3. Scrape Each Product Page
        products = []
        async with AsyncWebCrawler() as crawler:
            for url in product_links:
                print(f"[DAG] Scraping Product: {url}")
                try:
                    res = await crawler.arun(url=url)
                    if res.success:
                        # Simple extraction strategy (can be improved with LLM later)
                        # For now, we use the raw markdown or HTML to find price/title
                        # Title is usually the page title or h1
                        
                        # We need a robust way to extract. 
                        # Let's use a specialized prompt or just extraction for now.
                        # Ideally, we used the CSS selectors found in Phase 1.
                        # Since Crawl4AI returns markdown, we might need to parse HTML or use LLM.
                        # Let's use the LLM to "Extract Product Details" from the Markdown which is safer.
                        
                        extraction_prompt = f"""
                        Extract the following details from this product page markdown:
                        1. Product Title
                        2. Price (just the number and currency symbol)
                        3. Description (short summary)
                        4. Image URL (if any)
                        5. Product Category (e.g. Laptops, Cardiology, Loans, Appliances - Infer from context)

                        Markdown:
                        {res.markdown[:3000]}

                        Return JSON: {{ "title": "...", "price": "...", "description": "...", "image_url": "...", "category": "..." }}
                        """
                        
                        details = {}
                        try:
                            llm_res = await self.llm.chat.completions.create(
                                model=self.model_name,
                                messages=[{"role": "user", "content": extraction_prompt}],
                                response_format={"type": "json_object"} if "sonar" not in self.model_name and "llama" not in self.model_name.lower() else None
                            )
                            content = llm_res.choices[0].message.content
                            # Clean for local models
                            content = content.replace("```json", "").replace("```", "").strip()
                            details = json.loads(content)
                        except Exception as e:
                            print(f"[DAG] LLM Scrape Error: {e}. Using Regex fallback for {url}.")
                            # SIMPLE HEURISTIC FALLBACK
                            import re
                            product_md = res.markdown # Use the full markdown for regex
                            
                            title_match = re.search(r'^#\s+(.*)', product_md, re.MULTILINE)
                            title = title_match.group(1).strip() if title_match else url.split('/')[-1].replace('-', ' ').replace('_', ' ').title()
                            
                            # Look for price patterns like $12.99, 12.99%, £100, 1,234.56
                            price_match = re.search(r'(\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*%)|(\£\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?)|(\€\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?)', product_md)
                            price = price_match.group(0).strip() if price_match else "N/A"
                            
                            # Use first non-empty paragraph for description
                            desc_match = re.search(r'\n\n([^\n]+)\n', product_md)
                            description = desc_match.group(1).strip() if desc_match else "No description available."
                            
                            # Basic image URL extraction (looking for markdown image syntax)
                            image_match = re.search(r'!\[.*?\]\((.*?)\)', product_md)
                            image_url = image_match.group(1) if image_match else None
                            
                            details = {
                                "title": title,
                                "price": price,
                                "description": description,
                                "image_url": image_url,
                                "category": "General" # Fallback
                            }

                        if details: # Ensure details were extracted by either method
                            details['url'] = url
                            products.append(details)
                        
                except Exception as e:
                    print(f"[DAG] Failed to scrape {url}: {e}")

        # 4. Embed and Store in Qdrant + DB
        print(f"[DAG] Storing {len(products)} products in Qdrant...")
        if not products:
            print("[DAG] ❌ No products were scraped. Skipping Qdrant storage.")
            return

        try:
            # Local all-MiniLM-L6-v2 dimension is 384
            self.qdrant.create_collection_if_not_exists("dap_products", vector_size=384)
            
            from qdrant_client.models import PointStruct
            
            points = []
            for p in products:
                print(f"[DAG] Generating embedding for product: {p.get('title')}")
                # Generate Embedding
                text_to_embed = f"{p.get('title')} {p.get('description')} {p.get('price')} {p.get('category')}"
                vector = await self.embeddings.generate_embedding(text_to_embed)
                
                # Upsert to Qdrant
                point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, p['url']))
                points.append(PointStruct(id=point_id, vector=vector, payload={
                    "site_id": site_id,
                    "title": p.get('title'),
                    "price": p.get('price'),
                    "url": p['url'],
                    "description": p.get('description'),
                    "image_url": p.get('image_url'),
                    "category": p.get('category')
                }))
                
            if points:
                print(f"[DAG] Upserting {len(points)} points to Qdrant...")
                self.qdrant.upsert_points("dap_products", points)
                print(f"[DAG] ✅ Successfully indexed {len(points)} products in Qdrant.")

                # NEW: Persist to PostgreSQL
                try:
                    pool = await get_pool()
                    async with pool.acquire() as conn:
                        records = []
                        for p in products:
                            records.append((
                                uuid.UUID(str(site_id)),
                                p['url'],
                                "product",
                                str(uuid.uuid5(uuid.NAMESPACE_URL, p['url'])), # product_id
                                p.get('title'),
                                (p.get('description', '')[:200] + "...") if len(p.get('description', '')) > 200 else p.get('description', '')
                            ))
                        
                        await conn.executemany(
                            """
                            INSERT INTO dap.indexed_pages (site_id, url, page_type, product_id, title, snippet)
                            VALUES ($1, $2, $3, $4, $5, $6)
                            ON CONFLICT (site_id, url) DO UPDATE 
                            SET product_id = $4, title = $5, snippet = $6, indexed_at = now()
                            """,
                            records
                        )
                    print(f"[DAG-SQL] Recorded {len(records)} indexed pages in PostgreSQL")
                except Exception as e:
                    print(f"[DAG-SQL ERROR] Failed to record indexed pages: {e}")
        except Exception as e:
            print(f"[DAG] ❌ Qdrant/Embedding Error: {e}")
            import traceback
            traceback.print_exc()

