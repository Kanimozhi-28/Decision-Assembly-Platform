import asyncio
import asyncpg
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.config import Settings

async def seed_data():
    settings = Settings()
    try:
        conn = await asyncpg.connect(settings.database_url)
        # Check if any site exists
        row = await conn.fetchrow("SELECT id FROM dap.sites LIMIT 1")
        if not row:
            site_id = await conn.fetchval(
                "INSERT INTO dap.sites (name, base_url) VALUES ($1, $2) RETURNING id",
                "Demo Store", "http://localhost:8000"
            )
            await conn.execute(
                "INSERT INTO dap.site_config (site_id) VALUES ($1)",
                site_id
            )
            print(site_id)
        else:
            print(row['id'])
        await conn.close()
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(seed_data())
