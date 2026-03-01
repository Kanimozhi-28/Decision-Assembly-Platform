import asyncio
from app.db.database import get_pool

async def check():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name FROM dap.sites")
        for r in rows:
            print(dict(r))

if __name__ == "__main__":
    asyncio.run(check())
