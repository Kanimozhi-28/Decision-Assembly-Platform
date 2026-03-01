import asyncio
import asyncpg
import sys
import os
from pathlib import Path

# Add app to path
sys.path.append(str(Path(__file__).parent))

from app.config import Settings

async def verify():
    settings = Settings()
    print(f"Testing connection to: {settings.database_url}")
    try:
        conn = await asyncio.wait_for(asyncpg.connect(settings.database_url), timeout=5.0)
        print("Initial connection successful!")
        await conn.close()
        
        print("Testing pool creation...")
        pool = await asyncio.wait_for(asyncpg.create_pool(
            settings.database_url,
            min_size=1,
            max_size=2,
        ), timeout=5.0)
        print("Pool creation successful!")
        await pool.close()
        print("Verification COMPLETE.")
    except Exception as e:
        print(f"Verification FAILED: {e}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(verify())
