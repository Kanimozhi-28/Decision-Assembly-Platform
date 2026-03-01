import asyncio
import asyncpg
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.config import Settings

async def get_site_id():
    settings = Settings()
    try:
        conn = await asyncpg.connect(settings.database_url)
        row = await conn.fetchrow("SELECT id FROM dap.sites LIMIT 1")
        if row:
            id_str = str(row['id'])
            print(f"EXACT_ID_START:{id_str}:EXACT_ID_END")
        await conn.close()
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_site_id())
