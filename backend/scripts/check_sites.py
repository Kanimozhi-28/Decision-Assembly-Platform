import asyncio
import asyncpg
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app.config import Settings

async def check():
    settings = Settings()
    conn = await asyncpg.connect(settings.database_url)
    rows = await conn.fetch("SELECT id, name FROM dap.sites")
    for row in rows:
        print(f"ID: {row['id']} | Name: {row['name']}")
    await conn.close()

if __name__ == "__main__":
    asyncio.run(check())
