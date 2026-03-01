import asyncio
from app.services.qdrant_store import QdrantStore
from qdrant_client import models

async def check_qdrant():
    store = QdrantStore()
    collection_name = "dap_products"
    
    site_ids = [
        "88888888-8888-4888-8888-888888888888",
        "99999999-9999-4999-9999-999999999999",
        "77777777-7777-4777-7777-777777777777"
    ]
    
    collections = store.client.get_collections().collections
    exists = any(c.name == collection_name for c in collections)
    
    if not exists:
        print(f"Collection {collection_name} does not exist.")
        return

    for sid in site_ids:
        res = store.client.count(
            collection_name=collection_name,
            count_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="site_id",
                        match=models.MatchValue(value=sid)
                    )
                ]
            )
        )
        print(f"Site {sid}: {res.count} points")

if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    asyncio.run(check_qdrant())
