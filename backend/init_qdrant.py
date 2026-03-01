import requests
import json

def init_qdrant():
    url = "http://127.0.0.1:6333"
    collection_name = "apex_banking_products"
    
    print(f"🔍 Checking Qdrant at {url}...")
    try:
        response = requests.get(f"{url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Qdrant is up and running!")
        else:
            print(f"❌ Qdrant returned status code {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Could not connect to Qdrant: {e}")
        print("\n💡 Suggestion: Start Qdrant using Docker:")
        print("   docker run -p 6333:6333 qdrant/qdrant")
        return

    # Check if collection exists
    print(f"📦 Checking for collection '{collection_name}'...")
    response = requests.get(f"{url}/collections/{collection_name}")
    
    if response.status_code == 200:
        print(f"✨ Collection '{collection_name}' already exists.")
    else:
        print(f"🔨 Creating collection '{collection_name}'...")
        # v4 models usually output 384 or 768 dimensions. 
        # Mistral embeddings might vary, but for this demo, 
        # we'll use 768 (standard for many BERT-based models).
        payload = {
            "vectors": {
                "size": 768,
                "distance": "Cosine"
            }
        }
        create_response = requests.put(
            f"{url}/collections/{collection_name}",
            json=payload
        )
        if create_response.status_code == 200:
            print(f"✅ Collection '{collection_name}' created successfully!")
        else:
            print(f"❌ Failed to create collection: {create_response.text}")

if __name__ == "__main__":
    init_qdrant()
