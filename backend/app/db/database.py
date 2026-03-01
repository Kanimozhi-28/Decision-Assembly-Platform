import asyncpg
from app.config import Settings

settings = Settings()

pool: asyncpg.Pool | None = None

async def get_pool() -> asyncpg.Pool:
    global pool
    if pool is None:
        try:
            print(f"[DB] Creating pool for {settings.database_url}")
            pool = await asyncpg.create_pool(
                settings.database_url,
                min_size=2,
                max_size=10,
                command_timeout=10,
                timeout=5
            )
            print("[DB] Pool created.")
        except Exception as e:
            print(f"[DB] Failed to create pool: {e}")
            raise e
    return pool

async def close_pool():
    global pool
    if pool:
        await pool.close()
        pool = None
