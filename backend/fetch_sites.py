import asyncio
import asyncpg
import json
from app.db.database import get_pool

async def main():
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            rows = await conn.fetch("SELECT id, name, base_url FROM dap.sites")
            print("--- SITES FOUND ---")
            for r in rows:
                print(f"ID: {r['id']} | Name: {r['name']} | URL: {r['base_url']}")
            print("--- END SITES ---")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
