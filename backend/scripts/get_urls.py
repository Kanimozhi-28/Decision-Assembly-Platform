
import asyncio
from app.db.database import get_pool

async def get_test_urls():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT url FROM dap.indexed_pages WHERE site_id = '99999999-9999-4999-9999-999999999999' LIMIT 2")
        urls = [r['url'] for r in rows]
        print(urls)

if __name__ == "__main__":
    asyncio.run(get_test_urls())
