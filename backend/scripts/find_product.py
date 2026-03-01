import asyncio
import json
from app.services.qdrant_store import QdrantStore
import os
import sys
from qdrant_client import models

sys.path.append(os.getcwd())

async def find_product():
    q = QdrantStore()
    # Search for anything containing 'banking-' in the URL
    res = q.client.scroll(
        collection_name='dap_products',
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(key="url", match=models.MatchText(text="banking-max-saver"))
            ]
        ),
        limit=5
    )
    payloads = [p.payload for p in res[0]]
    print(json.dumps(payloads, indent=2))

if __name__ == "__main__":
    asyncio.run(find_product())
