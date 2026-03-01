import asyncio
import json
from app.db.database import get_pool
import os
import sys

# Ensure app can be imported
sys.path.append(os.getcwd())

async def list_urls():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT url FROM dap.indexed_pages')
        urls = [r['url'] for r in rows]
        print(json.dumps(urls, indent=2))
    await pool.close()

if __name__ == "__main__":
    asyncio.run(list_urls())
