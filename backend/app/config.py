from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    database_url: str
    qdrant_url: str = "http://10.100.20.76:6333"
    qdrant_api_key: str | None = None
    secret_key: str = "your-secret-key-here-for-local-dev-only"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 # 24 hours
    cors_origins: list[str] = ["*"]
    openai_api_key: str | None = None
    perplexity_api_key: str | None = None
    llm_base_url: str = "https://api.openai.com/v1"
    ollama_base_url: str | None = None
    ollama_model: str = "llama3"
    
    class Config:
        env_file = str(Path(__file__).resolve().parent.parent / ".env")
        env_file_encoding = "utf-8"
        extra = "ignore"
