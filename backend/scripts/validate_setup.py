import asyncio
import asyncpg
import os
from dotenv import load_dotenv

async def validate_system():
    print("--- DAP SYSTEM VALIDATION ---")
    
    # 1. Check .env
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")
    print(f"1. Checking Environment...")
    if not db_url:
        print("   [FAIL] DATABASE_URL is missing in .env")
        return
    print(f"   [PASS] DATABASE_URL found: {db_url}")
    
    if os.getenv("OPENAI_API_KEY") and "your-" not in os.getenv("OPENAI_API_KEY"):
         print("   [PASS] OPENAI_API_KEY is set")
    else:
         print("   [WARN] OPENAI_API_KEY is missing or default. Universal DAG will use fallback rules.")

    # 2. Check Database Connection
    print("\n2. Checking Database...")
    try:
        conn = await asyncpg.connect(db_url)
        print("   [PASS] Connection to PostgreSQL successful")
        
        # 3. Check Seeded Sites
        print("\n3. Checking Seeded Sites...")
        sites = await conn.fetch("SELECT id, name, base_url FROM dap.sites")
        if len(sites) == 0:
             print("   [FAIL] No sites found in DB! You need to run seed_demo_sites.py.")
        else:
             print(f"   [PASS] Found {len(sites)} sites in DB:")
             for site in sites:
                 print(f"      - {site['name']} (ID: {site['id']})")
                 
        await conn.close()
    except Exception as e:
        print(f"   [FAIL] DB Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(validate_system())
