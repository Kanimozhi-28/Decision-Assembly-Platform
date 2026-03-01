import sys
from pathlib import Path
# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

import asyncio
from app.db.database import get_pool
from app.services.embeddings import EmbeddingService
from app.services.qdrant_store import QdrantStore
from qdrant_client.models import PointStruct
import uuid

async def seed_demo_store():
    # Site ID from the HTML files in demo-store
    site_id = "f203f546-e89b-48da-8007-0653a57debab"
    pool = await get_pool()
    
    print(f"Seeding demo-store site {site_id}...")
    
    async with pool.acquire() as conn:
        # 1. Create Site
        await conn.execute("""
            INSERT INTO dap.sites (id, name, base_url)
            VALUES ($1, 'Forge Tech Store', 'http://localhost:5173')
            ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
        """, uuid.UUID(site_id))
        
        # 2. Create Site Config
        await conn.execute("""
            INSERT INTO dap.site_config (site_id, allowed_origins)
            VALUES ($1, '["*"]')
            ON CONFLICT (site_id) DO NOTHING
        """, uuid.UUID(site_id))

        # 3. Create Rationale Templates
        await conn.execute("""
            INSERT INTO dap.rationale_templates (site_id, intent, template_text)
            VALUES ($1, 'help_me_choose', 'The {product_name} is the gold standard for {feature} in its class.')
            ON CONFLICT DO NOTHING
        """, uuid.UUID(site_id))

    # 4. Seed Qdrant
    print("Seeding Qdrant for demo-store...")
    embeddings = EmbeddingService()
    qdrant = QdrantStore()
    collection_name = f"site_{site_id}"
    qdrant.create_collection_if_not_exists(collection_name)
    
    products = [
        {
            "title": "Chronos Elite Titan",
            "text": "The ultimate expression of titanium engineering. 455ppi sapphire display, 7-day battery, high-altitude biometric sensors.",
            "url": "http://localhost:5173/demo-store/product-watch.html",
            "product_id": "watch-p1",
            "price": "$1,299"
        },
        {
            "title": "Audio-X Carbon",
            "text": "Studio-grade audio with carbon fiber drivers. Active noise cancellation and 40-hour battery life. Lightweight and durable.",
            "url": "http://localhost:5173/demo-store/product-headphones.html",
            "product_id": "headphones-p2",
            "price": "$599"
        },
        {
            "title": "Nebula Air 14",
            "text": "Ultralight laptop with a liquid retina display. Powered by the M3 Pro chip for uncompromising performance and portability.",
            "url": "http://localhost:5173/demo-store/product-laptop.html",
            "product_id": "laptop-p3",
            "price": "$2,499"
        }
    ]
    
    points = []
    for i, p in enumerate(products):
        vector = await embeddings.generate_embedding(f"{p['title']} {p['text']}")
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={
                "site_id": site_id,
                "url": p["url"],
                "title": p["title"],
                "text": p["text"],
                "product_id": p["product_id"],
                "price": p["price"]
            }
        ))
    
    qdrant.upsert_points(collection_name, points)
    print("Demo-store seed complete!")

if __name__ == "__main__":
    asyncio.run(seed_demo_store())
