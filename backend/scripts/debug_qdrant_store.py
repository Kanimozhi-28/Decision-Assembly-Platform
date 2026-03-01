import sys
from pathlib import Path
import asyncio

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.qdrant_store import QdrantStore
from qdrant_client import models

async def debug_store():
    store = QdrantStore()
    print("Store initialized.")
    
    collection_name = "dap_products"
    url = "http://localhost:8000/test-sites/banking/banking-kids-junior-account.html"
    
    print(f"Searching for URL: {url}")
    
    # Try 1: Scroll with Filter
    try:
        res = store.client.scroll(
            collection_name=collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(key="url", match=models.MatchValue(value=url))
                ]
            ),
            limit=1
        )
        points, _ = res
        print(f"Method 1 (Scroll MatchValue): Found {len(points)} points")
        if points:
            print(f" - ID: {points[0].id}")
            print(f" - Payload: {points[0].payload}")
    except Exception as e:
        print(f"Method 1 Failed: {e}")

    # Try 2: Scroll with MatchText
    try:
        res = store.client.scroll(
            collection_name=collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(key="url", match=models.MatchText(text=url))
                ]
            ),
            limit=1
        )
        points, _ = res
        print(f"Method 2 (Scroll MatchText): Found {len(points)} points")
    except Exception as e:
        print(f"Method 2 Failed: {e}")

    # Try 3: Scroll with Site ID
    try:
        site_id = "99999999-9999-4999-9999-999999999999"
        print(f"Searching for Site ID: {site_id}")
        res = store.client.scroll(
            collection_name=collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(key="site_id", match=models.MatchValue(value=site_id))
                ]
            ),
            limit=10
        )
        points, _ = res
        print(f"Method 3 (Scroll SiteID): Found {len(points)} points")
        for p in points:
            print(f" - Found: {p.payload.get('title')} ({p.payload.get('url')})")
    except Exception as e:
        print(f"Method 3 Failed: {e}")

if __name__ == "__main__":
    asyncio.run(debug_store())
