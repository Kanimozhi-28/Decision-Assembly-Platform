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

async def seed_data():
    site_id = "de305d54-75b4-431b-adb2-eb6b9e546014"
    pool = await get_pool()
    
    print(f"Seeding site {site_id}...")
    
    async with pool.acquire() as conn:
        # 1. Create Site
        await conn.execute("""
            INSERT INTO dap.sites (id, name, base_url)
            VALUES ($1, 'DAP Demo Store', 'http://localhost:5173')
            ON CONFLICT (id) DO NOTHING
        """, uuid.UUID(site_id))
        
        # 2. Create Site Config
        await conn.execute("""
            INSERT INTO dap.site_config (site_id, allowed_origins)
            VALUES ($1, '["*"]')
            ON CONFLICT (site_id) DO NOTHING
        """, uuid.UUID(site_id))

        # 3. Create a Rationale Template
        await conn.execute("""
            INSERT INTO dap.rationale_templates (site_id, intent, template_text)
            VALUES ($1, 'help_me_choose', 'This {product_name} is a great choice because it matches your focus on {feature}.')
            ON CONFLICT DO NOTHING
        """, uuid.UUID(site_id))

    # 4. Seed Qdrant
    print("Seeding Qdrant...")
    embeddings = EmbeddingService()
    qdrant = QdrantStore()
    collection_name = f"site_{site_id}"
    qdrant.create_collection_if_not_exists(collection_name)
    
    products = [
        {
            "title": "Premium Wireless Headphones",
            "text": "Active noise cancelling, 30-hour battery life, superb sound quality. Ideal for travel and office work.",
            "url": "http://localhost:5173/products/headphones-p1",
            "product_id": "p1",
            "price": "$299"
        },
        {
            "title": "Ergonomic Mechanical Keyboard",
            "text": "RGB backlit, Cherry MX switches, programmable macros. Perfect for developers and gamers who value comfort.",
            "url": "http://localhost:5173/products/keyboard-p2",
            "product_id": "p2",
            "price": "$159"
        },
        {
            "title": "Ultra-Wide 4K Monitor",
            "text": "34-inch curved display, 144Hz refresh rate, HDR support. Excellent for multi-tasking and immersive media.",
            "url": "http://localhost:5173/products/monitor-p3",
            "product_id": "p3",
            "price": "$699"
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
    print("Seed complete!")

if __name__ == "__main__":
    asyncio.run(seed_data())
