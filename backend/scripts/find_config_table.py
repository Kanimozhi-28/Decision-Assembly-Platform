import asyncio
import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def find_config_table():
    pool = await get_pool()
    async with pool.acquire() as conn:
        print("Searching for 'site_config' table...")
        rows = await conn.fetch("""
            SELECT table_schema, table_name 
            FROM information_schema.tables 
            WHERE table_name = 'site_config'
        """)
        for r in rows:
            print(f"Found: {r['table_schema']}.{r['table_name']}")
            cols = await conn.fetch(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_schema = '{r['table_schema']}' AND table_name = 'site_config'
            """)
            for c in cols:
                print(f"  - {c['column_name']} ({c['data_type']})")

if __name__ == "__main__":
    asyncio.run(find_config_table())
