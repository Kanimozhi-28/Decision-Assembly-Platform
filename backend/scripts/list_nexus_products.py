import asyncio
import json
from app.services.qdrant_store import QdrantStore
import os
import sys
from qdrant_client import models

sys.path.append(os.getcwd())

async def list_nexus_products():
    q = QdrantStore()
    site_id = "99999999-9999-4999-9999-999999999999"
    res = q.client.scroll(
        collection_name='dap_products',
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(key="site_id", match=models.MatchValue(value=site_id))
            ]
        ),
        limit=100
    )
    payloads = [p.payload for p in res[0]]
    print(json.dumps(payloads, indent=2))

if __name__ == "__main__":
    asyncio.run(list_nexus_products())
