import json
import requests
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Configuration
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
ollama_base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
if ollama_base.endswith("/v1"):
    ollama_base = ollama_base[:-3]
OLLAMA_URL = ollama_base

EMBEDDING_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text") 

def get_embedding(text):
    """Get vector embedding from Ollama"""
    url = f"{OLLAMA_URL}/api/embeddings"
    payload = {
        "model": "nomic-embed-text",
        "prompt": text
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("embedding")
        else:
            print(f"Ollama returned error: {response.text}")
            return None
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        return None

def ensure_collection(collection_name):
    """Ensure Qdrant collection exists"""
    resp = requests.get(f"{QDRANT_URL}/collections/{collection_name}")
    if resp.status_code != 200:
        print(f"Creating collection: {collection_name}...")
        create_payload = {
            "vectors": {
                "size": 768, # nomic-embed-text size
                "distance": "Cosine"
            }
        }
        requests.put(f"{QDRANT_URL}/collections/{collection_name}", json=create_payload)

def index_site_content(site_id):
    input_file = Path(f"crawled_{site_id}.json")
    
    if not input_file.exists():
        print(f"Error: {input_file} not found. Run 'python backend/crawler.py --site_id {site_id}' first.")
        return

    # Collection naming convention: dap_uuid
    collection_name = f"dap_{site_id.replace('-', '_')}"
    ensure_collection(collection_name)

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Indexing {len(data)} pages into collection: {collection_name}...")

    for page_idx, item in enumerate(data):
        url = item.get("url")
        content = item.get("content", "")
        title = item.get("title") or item.get("path") or "Untitled Page"
        
        # INFERENCE: Extract category from URL
        path_parts = [p for p in url.split('/') if p and p not in ['http:', 'https:', 'localhost:5173', 'localhost:5174', '127.0.0.1:5173', '127.0.0.1:5174']]
        category = path_parts[0] if path_parts else "general"

        # CHUNKING LOGIC: Sliding window (TAD §11.4.3 Alignment)
        # Window size: 1200 chars (~300 tokens), Overlap: 300 chars
        chunk_size = 1200
        overlap = 300
        chunks = []
        
        if len(content) <= chunk_size:
            chunks.append(content)
        else:
            start = 0
            while start < len(content):
                end = start + chunk_size
                chunks.append(content[start:end])
                start += (chunk_size - overlap)
                if start >= len(content) - overlap: # Avoid tiny tail chunks
                    break

        print(f"   [{page_idx+1}/{len(data)}] Indexing {url} ({len(chunks)} chunks)...")

        for chunk_idx, chunk_text in enumerate(chunks):
            embedding = get_embedding(chunk_text)
            
            if not embedding:
                print(f"      ❌ Chunk {chunk_idx} failed.")
                continue

            # ENRICHMENT: Map metadata to payload
            meta = item.get("metadata", {})
            
            # Deterministic ID combining page index and chunk index
            point_id = (page_idx + 1) * 1000 + chunk_idx
            
            point = {
                "points": [
                    {
                        "id": point_id,
                        "vector": embedding,
                        "payload": {
                            "url": url,
                            "title": title,
                            "category": category,
                            "content_preview": chunk_text[:500],
                            "site_id": site_id,
                            "chunk_index": chunk_idx,
                            "price": meta.get("price"),
                            "features": meta.get("features", []),
                            "indexed_at": Path(input_file).stat().st_mtime
                        }
                    }
                ]
            }

            requests.put(f"{QDRANT_URL}/collections/{collection_name}/points", json=point)

    print(f"\nIndexing for {site_id} complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generic Indexer for DAP")
    parser.add_argument("--site_id", type=str, required=True, help="Site ID (UUID)")
    
    args = parser.parse_args()
    index_site_content(args.site_id)
