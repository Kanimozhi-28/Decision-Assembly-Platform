import sys
import os
import asyncio

# Add parent directory to path to import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.qdrant_store import QdrantStore
from qdrant_client import models

async def check_qdrant_categories():
    store = QdrantStore()
    collection_name = "dap_products"
    
    print(f"=== QDRANT CATEGORY AUDIT ({collection_name}) ===")
    
    try:
        # Scroll through all points
        res = store.client.scroll(
            collection_name=collection_name,
            limit=100,
            with_payload=True,
            with_vectors=False
        )
        points, _ = res
        
        # Group by site and category
        audit = {}
        for p in points:
            payload = p.payload
            site_id = payload.get("site_id", "Unknown")
            category = payload.get("category", "General")
            title = payload.get("title", "Untitled")
            
            if site_id not in audit:
                audit[site_id] = {}
            if category not in audit[site_id]:
                audit[site_id][category] = []
            
            audit[site_id][category].append(title)
            
        for site, categories in audit.items():
            print(f"\nSite: {site}")
            for cat, titles in categories.items():
                print(f"  [{cat}] ({len(titles)} products):")
                for t in titles[:5]:
                    print(f"    - {t}")
                if len(titles) > 5:
                    print(f"    ... and {len(titles) - 5} more")
                    
    except Exception as e:
        print(f"Error checking Qdrant: {e}")

if __name__ == "__main__":
    asyncio.run(check_qdrant_categories())
