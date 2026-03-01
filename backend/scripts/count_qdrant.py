import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.qdrant_store import QdrantStore
from qdrant_client import models

try:
    store = QdrantStore()
    collection_name = "dap_products"
    collections = store.client.get_collections()
    print(f"Collections: {collections}")
    
    exists = any(c.name == collection_name for c in collections.collections)
    if exists:
        info = store.client.get_collection(collection_name)
        print(f"Collection '{collection_name}' has {info.points_count} points.")
    else:
        print(f"Collection '{collection_name}' does not exist.")
except Exception as e:
    print(f"Error: {e}")
