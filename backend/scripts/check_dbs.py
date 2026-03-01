import asyncio
import asyncpg

async def list_dbs():
    try:
        conn = await asyncpg.connect("postgresql://postgres:password@localhost:5432/postgres")
        rows = await conn.fetch("SELECT datname FROM pg_database;")
        print("Available databases:")
        for row in rows:
            print(f"- '{row['datname']}'")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(list_dbs())
