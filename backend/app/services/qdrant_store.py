from app.config import Settings
from typing import Any, Optional

settings = Settings()

class QdrantStore:
    def __init__(self):
        # Handle empty API key strings from .env (common issue with local setups)
        from qdrant_client import QdrantClient
        api_key = settings.qdrant_api_key
        if api_key and not api_key.strip():
            api_key = None
            
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=api_key,
            prefer_grpc=False,
            timeout=10
        )
        print(f"[QDRANT] Initialized client at {settings.qdrant_url}")

    def create_collection_if_not_exists(self, collection_name: str, vector_size: int = 384):
        from qdrant_client import models
        collections = self.client.get_collections().collections
        exists = any(c.name == collection_name for c in collections)
        
        if not exists:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE
                )
            )

    def upsert_points(self, collection_name: str, points: list):
        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

    def search(self, collection_name: str, vector: list[float], limit: int = 5, score_threshold: float | None = None, query_filter: Any = None):
        # Using query_points instead of search as per Qdrant 1.0+ client changes
        result = self.client.query_points(
            collection_name=collection_name,
            query=vector,
            limit=limit,
            score_threshold=score_threshold,
            query_filter=query_filter
        )
        return result.points
