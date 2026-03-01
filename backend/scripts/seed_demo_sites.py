import asyncio
import uuid

async def seed_demo_sites():
    from app.db.database import get_pool
    print("Seeding demo sites...")
    pool = await get_pool()
    
    sites = [
        ("88888888-8888-4888-8888-888888888888", "E-Life Store", "http://localhost:8000/test-sites/ecommerce"),
        ("99999999-9999-4999-9999-999999999999", "Nexus Digital Bank", "http://localhost:8000/test-sites/banking"),
        ("77777777-7777-4777-7777-777777777777", "CarePoint Healthcare", "http://localhost:8000/test-sites/healthcare")
    ]
    
    async with pool.acquire() as conn:
        for site_id, name, url in sites:
            # Check if exists
            exists = await conn.fetchval("SELECT 1 FROM dap.sites WHERE id = $1", uuid.UUID(site_id))
            if not exists:
                await conn.execute(
                    "INSERT INTO dap.sites (id, name, base_url) VALUES ($1, $2, $3)",
                    uuid.UUID(site_id), name, url
                )
                await conn.execute(
                    "INSERT INTO dap.site_config (site_id) VALUES ($1)",
                    uuid.UUID(site_id)
                )
                print(f"Registered site: {name}")
            else:
                print(f"Site {name} already exists.")

    print("Seeding complete.")

if __name__ == "__main__":
    import os
    import sys
    # Add backend root to sys.path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    asyncio.run(seed_demo_sites())
