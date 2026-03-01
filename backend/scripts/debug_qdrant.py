from qdrant_client import QdrantClient
from app.config import Settings
import json

settings = Settings()
client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)

try:
    info = client.get_collection("dap_products")
    print(f"Collection 'dap_products' exists. Points count: {info.points_count}")
    
    if info.points_count > 0:
        res = client.scroll(
            collection_name="dap_products",
            limit=5,
            with_payload=True,
            with_vectors=False
        )
        print("\n--- SAMPLE POINTS ---")
        for point in res[0]:
            print(f"ID: {point.id}")
            print(f"Payload: {json.dumps(point.payload, indent=2)}")
    else:
        print("\n[WARNING] Collection is empty! Sync failed to index anything.")

except Exception as e:
    print(f"Error accessing Qdrant: {e}")
