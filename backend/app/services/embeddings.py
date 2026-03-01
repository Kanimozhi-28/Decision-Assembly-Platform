from app.config import Settings
import asyncio
import os

class EmbeddingService:
    _model = None

    def __init__(self, model_name: str = 'BAAI/bge-small-en-v1.5'):
        self.settings = Settings()
        self.model_name = model_name
        # Lazy load: Do nothing here

    @classmethod
    def get_model(cls, model_name: str = 'BAAI/bge-small-en-v1.5'):
        if cls._model is None:
            print(f"Loading local Embedding Model: {model_name}...")
            # Disable progress bars to avoid [Errno 22] flash error on Windows
            os.environ["TQDM_DISABLE"] = "True"
            try:
                import transformers
                transformers.utils.logging.disable_progress_bar()
            except:
                pass
            from sentence_transformers import SentenceTransformer
            cls._model = SentenceTransformer(model_name)
            print(f"Embedding Service initialized with local model: {model_name}")
        return cls._model

    async def generate_embedding(self, text: str) -> list[float]:
        """
        Generates an embedding for the given text using local SentenceTransformer.
        """
        # Run in thread pool to avoid blocking async loop
        loop = asyncio.get_event_loop()
        # Use class method to ensure model is loaded
        model = EmbeddingService.get_model(self.model_name)
        embedding = await loop.run_in_executor(None, lambda: model.encode(text))
        return embedding.tolist()

    async def generate_embeddings_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Generates embeddings for a batch of texts using local SentenceTransformer.
        """
        loop = asyncio.get_event_loop()
        model = EmbeddingService.get_model(self.model_name)
        embeddings = await loop.run_in_executor(None, lambda: model.encode(texts))
        return embeddings.tolist()
