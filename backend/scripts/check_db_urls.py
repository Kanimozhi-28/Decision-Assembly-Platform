import asyncio
import uuid
import sys
import os

# Add parent directory to path to import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def check_urls():
    pool = await get_pool()
    async with pool.acquire() as conn:
        print("=== DATABASE URL CHECK ===")
        sites = await conn.fetch("SELECT id, name, base_url FROM dap.sites")
        for site in sites:
            print(f"\nSite: {site['name']} ({site['base_url']})")
            # indexed_pages doesn't have category, we might need to check site_config or join with something
            # Actually, indexed_pages has 'snippet', but 'category' is in Qdrant payload.
            # Let's check PostgreSQL indexed_pages first for a general view.
            rows = await conn.fetch("SELECT title, url, product_id FROM dap.indexed_pages WHERE site_id = $1", site['id'])
            for r in rows:
                print(f"  {r['title']} | ID: {r['product_id']} | {r['url']}")

if __name__ == "__main__":
    asyncio.run(check_urls())
