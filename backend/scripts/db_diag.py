import asyncio
import asyncpg
import sys

async def check_db():
    print("Testing connection to 'postgres' database...")
    try:
        # Connect to 'postgres' to check for other DBs
        conn = await asyncpg.connect("postgresql://postgres:password@localhost:5432/postgres")
        print("Successfully connected to 'postgres'")
        
        databases = await conn.fetch("SELECT datname FROM pg_database WHERE datistemplate = false;")
        print("Existing databases:")
        for db in databases:
            print(f" - '{db['datname']}'")
            
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(check_db())
