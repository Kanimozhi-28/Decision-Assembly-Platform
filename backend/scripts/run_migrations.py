import asyncio
import asyncpg
import os
import sys
from pathlib import Path

# Add backend to path to import config
sys.path.append(str(Path(__file__).parent.parent))
from app.config import Settings

async def run_migrations():
    settings = Settings()
    print(f"Connecting to {settings.database_url}...")
    try:
        conn = await asyncpg.connect(settings.database_url)
    except Exception as e:
        print(f"Error connecting to DB: {e}")
        return

    migrations_dir = Path(__file__).parent.parent / "migrations"
    
    print(f"Looking for migrations in {migrations_dir}")
    for sql_file in sorted(migrations_dir.glob("*.sql")):
        print(f"Running {sql_file.name}...")
        sql = sql_file.read_text()
        try:
            await conn.execute(sql)
            print("  Done.")
        except Exception as e:
            print(f"  Error running migration {sql_file.name}: {e}")
            await conn.close()
            return

    await conn.close()
    print("Migrations complete!")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_migrations())
