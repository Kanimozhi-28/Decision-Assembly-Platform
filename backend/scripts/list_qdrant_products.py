from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(url="http://10.100.20.76:6333")
collection_name = "dap_products"

try:
    # Scroll through all points
    res, _ = client.scroll(
        collection_name=collection_name,
        limit=100,
        with_payload=True,
        with_vectors=False
    )
    
    print(f"Found {len(res)} products in Qdrant.")
    for p in res:
        payload = p.payload
        print(f"ID: {p.id} | Title: {payload.get('title')} | URL: {payload.get('url')} | SiteID: {payload.get('site_id')}")

except Exception as e:
    print(f"Error: {e}")
