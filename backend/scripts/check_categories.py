import asyncio
import json
from app.db.database import get_pool
import os
import sys

sys.path.append(os.getcwd())

async def check_categories():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT category, url FROM dap.indexed_pages')
        data = [{'category': r['category'], 'url': r['url']} for r in rows]
        print(json.dumps(data, indent=2))
    await pool.close()

if __name__ == "__main__":
    asyncio.run(check_categories())
