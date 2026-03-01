from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
import uuid

router = APIRouter(prefix="/search", tags=["search"])

class SearchRequest(BaseModel):
    query: str
    site_id: str
    limit: int = 5

@router.post("/")
async def search(request: SearchRequest):
    try:
        # Validate UUID
        uuid.UUID(request.site_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid site_id UUID")

    # Generate embedding for the query
    embedding_service = EmbeddingService()
    query_vector = await embedding_service.generate_embedding(request.query)

    # Search in Qdrant
    qdrant = QdrantStore()
    collection_name = f"site_{request.site_id}"
    
    # Check if collection exists first/handle error
    search_results = qdrant.search(collection_name, query_vector, limit=request.limit)
    
    # Format results
    results = []
    for hit in search_results:
        results.append({
            "score": hit.score,
            "text": hit.payload.get("text"),
            "title": hit.payload.get("title"),
            "url": hit.payload.get("url")
        })
        
    return {"results": results}
