import asyncio
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.indexing import IndexingService
import uuid

async def test_pipeline():
    print("Initializing Indexing Service...")
    indexer = IndexingService()
    
    test_url = "https://example.com"
    test_site_id = str(uuid.uuid4())
    
    print(f"Starting test crawl for {test_url} (Site ID: {test_site_id})")
    print("Step 1: Fetching & Extracting...")
    # We call index_url which wraps the whole pipeline
    result = await indexer.index_url(test_url, test_site_id)
    
    print("Pipeline Result:")
    print(result)
    
    if result.get("status") == "success":
        print("\nStep 2: Verifying in Qdrant...")
        # Verify it's there
        collection_name = f"site_{test_site_id}"
        # Search for "domain" to see if we get the example domain text
        search_result = indexer.qdrant.search(collection_name, [0.1]*384, limit=1) # Dummy vector for now or rely on keyword if we had it
        # Actually proper verification needs a real query vector.
        # Let's generate one.
        query_vec = await indexer.embeddings.generate_embedding("domain")
        search_result = indexer.qdrant.search(collection_name, query_vec, limit=1)
        
        print(f"Search found {len(search_result)} results.")
        if search_result:
            print(f"Top result score: {search_result[0].score}")
            print(f"Payload: {search_result[0].payload}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(test_pipeline())
