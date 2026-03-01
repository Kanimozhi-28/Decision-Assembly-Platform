import asyncio
import json
from app.db.database import get_pool
import os
import sys

sys.path.append(os.getcwd())

async def check_site_ids():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT site_id, url FROM dap.indexed_pages')
        data = [{'site_id': str(r['site_id']), 'url': r['url']} for r in rows]
        print(json.dumps(data, indent=2))
    await pool.close()

if __name__ == "__main__":
    asyncio.run(check_site_ids())
