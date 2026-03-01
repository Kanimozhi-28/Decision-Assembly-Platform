import asyncio
import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def list_tables():
    pool = await get_pool()
    async with pool.acquire() as conn:
        print("Tables in 'dap' schema:")
        rows = await conn.fetch("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'dap'
        """)
        for r in rows:
            t = r['table_name']
            print(f"\nTable: {t}")
            cols = await conn.fetch("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_schema = 'dap' AND table_name = $1
            """, t)
            for c in cols:
                print(f"  - {c['column_name']} ({c['data_type']})")

if __name__ == "__main__":
    asyncio.run(list_tables())
