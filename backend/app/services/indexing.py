from app.services.crawler import CrawlerService
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
from app.db.database import get_pool
import uuid
import uuid as uuid_lib

class IndexingService:
    def __init__(self):
        self.crawler = CrawlerService()
        self.embeddings = EmbeddingService()
        self.qdrant = QdrantStore()

    def _extract_metadata(self, text: str) -> dict:
        """
        Heuristic extraction of price and features from text.
        """
        import re
        meta = {"price": "N/A", "features": []}
        
        # simple price regex: $123 or $123.45 or ₹123
        price_match = re.search(r'[\$\₹]\s?[\d,]+(?:\.\d{2})?', text)
        if price_match:
            meta["price"] = price_match.group(0)
            
        # simple features: lines starting with dash or bullet
        features = []
        for line in text.split('\n'):
            line = line.strip()
            if line.startswith(('-', '•', '*')) and len(line) > 5:
                features.append(line.lstrip('-•* ').strip())
        
        if features:
            meta["features"] = features[:5] # limit to 5
            
        return meta

    async def index_url(self, url: str, site_id: str):
        """
        Full pipeline: Fetch -> Extract -> Chunk -> Embed -> Store
        Unique ID generation: uuid5(url + chunk_index)
        """
        print(f"Fetching {url}...")
        html = await self.crawler.fetch_page(url)
        if not html:
            return {"status": "error", "message": "Failed to fetch page"}
        
        content = self.crawler.extract_content(html)
        text = content["text"]
        title = content["title"]
        
        # Simple chunking (by paragraphs for now)
        chunks = [c.strip() for c in text.split('\n\n') if len(c.strip()) > 50]
        
        points = []
        print(f"Generating embeddings for {len(chunks)} chunks...")
        
        from qdrant_client.models import PointStruct
        
        # Product ID is typically derived from the URL
        # We'll use uuid5 of the URL itself as the base product_id
        product_id = str(uuid_lib.uuid5(uuid_lib.NAMESPACE_URL, url))

        for i, chunk in enumerate(chunks):
            vector = await self.embeddings.generate_embedding(chunk)
            meta = self._extract_metadata(chunk)
            
            # Deterministic Chunk ID
            chunk_id = str(uuid_lib.uuid5(uuid_lib.NAMESPACE_URL, f"{url}_{i}"))
            
            point = PointStruct(
                id=chunk_id,
                vector=vector,
                payload={
                    "site_id": str(site_id),
                    "product_id": product_id, 
                    "url": url,
                    "title": title,
                    "text": chunk,
                    "chunk_index": i,
                    "price": meta["price"],
                    "features": meta["features"],
                    "category": "general" # Default
                }
            )
            points.append(point)
            
        if points:
            # Ensure collection exists
            collection_name = "dap_products" # Use single collection for RAG demo
            self.qdrant.create_collection_if_not_exists(collection_name)
            
            self.qdrant.upsert_points(collection_name, points)
            print(f"Indexed {len(points)} chunks for {url}")

            # NEW: Persist to PostgreSQL
            try:
                pool = await get_pool()
                async with pool.acquire() as conn:
                    # Save a summary record of the page
                    await conn.execute(
                        """
                        INSERT INTO dap.indexed_pages (site_id, url, page_type, product_id, title, snippet)
                        VALUES ($1, $2, $3, $4, $5, $6)
                        ON CONFLICT (site_id, url) DO UPDATE 
                        SET product_id = $4, title = $5, snippet = $6, indexed_at = now()
                        """,
                        uuid_lib.UUID(str(site_id)),
                        url,
                        "product",
                        product_id,
                        title,
                        (text[:200] + "...") if len(text) > 200 else text
                    )
                print(f"[SQL] Recorded indexed page: {url}")
            except Exception as e:
                print(f"[SQL ERROR] Failed to record indexed page: {e}")

            return {"status": "success", "chunks_indexed": len(points)}
            
        return {"status": "warning", "message": "No content found to index"}
