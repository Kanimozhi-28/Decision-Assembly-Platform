import asyncio
import json
import os
import sys

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.qdrant_store import QdrantStore

async def check_qdrant_payloads():
    q = QdrantStore()
    res = q.client.scroll(collection_name='dap_products', limit=15)
    payloads = [p.payload for p in res[0]]
    print(json.dumps(payloads, indent=2))

if __name__ == "__main__":
    asyncio.run(check_qdrant_payloads())
