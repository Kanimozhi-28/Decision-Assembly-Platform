import asyncio
import uuid
import sys
import os
import json

# Add parent directory to path to import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool, close_pool
from app.services.qdrant_store import QdrantStore

async def audit():
    print("=== DAP GRID READINESS AUDIT ===")
    pool = await get_pool()
    qdrant = QdrantStore()
    
    async with pool.acquire() as conn:
        sites = await conn.fetch("SELECT id, name, base_url FROM dap.sites")
        
        for site in sites:
            s_id = site['id']
            name = site['name']
            url = site['base_url']
            
            print(f"\nSite: {name}")
            print(f"ID: {s_id}")
            print(f"Base URL: {url}")
            
            # Check Config
            config = await conn.fetchrow("SELECT block_mapping, product_page_rules FROM dap.site_config WHERE site_id = $1", s_id)
            if config:
                print(f"  [DB] Config: Found")
                print(f"  [DB] Block Mapping: {len(json.loads(config['block_mapping'])) if config['block_mapping'] else 0} intents mapped")
                print(f"  [DB] rules: {config['product_page_rules']}")
            else:
                print(f"  [DB] Config: MISSING")
            
            # Check Indexed Pages
            p_count = await conn.fetchval("SELECT count(*) FROM dap.indexed_pages WHERE site_id = $1", s_id)
            print(f"  [DB] Indexed Pages: {p_count}")
            
            # Check Qdrant
            # QdrantStore uses site_id in payload. We might need to filter.
            # However, search requires a vector. Let's just check if we can count by filter.
            try:
                # Qdrant client is self.client in QdrantStore
                collection_name = "dap_products"
                from qdrant_client import models
                res = qdrant.client.count(
                    collection_name=collection_name,
                    count_filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="site_id",
                                match=models.MatchValue(value=str(s_id)),
                            )
                        ]
                    )
                )
                print(f"  [QDRANT] Vectors: {res.count}")
            except Exception as e:
                print(f"  [QDRANT] Error: {e}")

    await close_pool()

if __name__ == "__main__":
    asyncio.run(audit())
