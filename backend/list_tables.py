import asyncio
from app.db.database import get_pool

async def list_all_tables():
    pool = await get_pool()
    async with pool.acquire() as conn:
        # Get all tables in dap schema
        tables = await conn.fetch("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'dap'
            ORDER BY table_name
        """)
        
        print("=" * 60)
        print("DATABASE TABLES AND ROW COUNTS")
        print("=" * 60)
        
        for table in tables:
            table_name = table['table_name']
            count = await conn.fetchval(f"SELECT COUNT(*) FROM dap.{table_name}")
            
            status = "[HAS DATA]" if count > 0 else "[EMPTY]"
            print(f"\n{status:15} | dap.{table_name}")
            print(f"                  Rows: {count}")
            
            if count > 0 and count <= 10:
                # Show sample data for small tables
                rows = await conn.fetch(f"SELECT * FROM dap.{table_name} LIMIT 3")
                if rows:
                    print(f"                  Sample columns: {list(rows[0].keys())}")

if __name__ == "__main__":
    asyncio.run(list_all_tables())
