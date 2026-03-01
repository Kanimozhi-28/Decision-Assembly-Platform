import asyncio
import asyncpg

async def fix_db_name():
    print("Connecting to 'postgres' to rename database...")
    try:
        conn = await asyncpg.connect("postgresql://postgres:password@localhost:5432/postgres")
        
        # Disconnect any other sessions if necessary (not usually needed for just renaming but safer)
        # Note: You can't rename a database if people are connected to it.
        
        print("Terminating other sessions for ' dap_db'...")
        await conn.execute("""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = ' dap_db'
              AND pid <> pg_backend_pid();
        """)
        
        print("Renaming ' dap_db' to 'dap_db'...")
        await conn.execute('ALTER DATABASE " dap_db" RENAME TO dap_db;')
        print("Successfully renamed database!")
        
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(fix_db_name())
