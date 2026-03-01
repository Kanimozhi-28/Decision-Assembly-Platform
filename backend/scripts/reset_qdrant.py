import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.qdrant_store import QdrantStore

async def reset_qdrant():
    print("Resetting Qdrant Collection 'dap_products'...")
    q = QdrantStore()
    q.client.delete_collection("dap_products")
    print("Collection deleted.")

if __name__ == "__main__":
    asyncio.run(reset_qdrant())
