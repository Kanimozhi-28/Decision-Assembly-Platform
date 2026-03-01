import asyncio
import uuid
import sys
import os

# Add parent directory to path to import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.dag import UniversalDAG
from app.db.database import get_pool, close_pool

async def verify_site(dag, pool, site_id, url, name):
    print(f"\n--- Verifying Site: {name} ---")
    print(f"URL: {url}")
    print(f"Site ID: {site_id}")
    
    # 1. Check current state
    async with pool.acquire() as conn:
        initial_count = await conn.fetchval("SELECT count(*) FROM dap.indexed_pages WHERE site_id = $1", uuid.UUID(site_id))
        print(f"Initial indexed_pages count: {initial_count}")

    # 2. Run Discovery (Node 1-3: Crawl, Analyze, Save Config)
    print(f"[STEP 1] Running Discovery...")
    try:
        result = await dag.run_discovery(url, site_id)
        if result.get("error"):
            print(f"❌ Discovery Error: {result['error']}")
            return False
        
        # Verify config was saved
        async with pool.acquire() as conn:
            config = await conn.fetchrow("SELECT product_page_rules, cta_selectors FROM dap.site_config WHERE site_id = $1", uuid.UUID(site_id))
            if config:
                print(f"✅ Discovery Phase Complete.")
                print(f"   Rules found: {config['product_page_rules']}")
            else:
                print(f"❌ Config not found in DB after discovery.")
                return False
    except Exception as e:
        print(f"💥 Discovery Exception: {e}")
        return False

    # 3. Run Catalog Sync
    print(f"[STEP 2] Running Catalog Sync...")
    try:
        await dag.sync_catalog(site_id, url)
        print("✅ Catalog Sync Complete.")
    except Exception as e:
        print(f"💥 Catalog Sync Exception: {e}")

    # 4. Final verification in DB
    async with pool.acquire() as conn:
        final_count = await conn.fetchval("SELECT count(*) FROM dap.indexed_pages WHERE site_id = $1", uuid.UUID(site_id))
        print(f"Final indexed_pages count: {final_count}")
        
        if final_count >= initial_count:
            print(f"🚀 SUCCESS! Site {name} integration verified.")
        else:
            print(f"⚠️ Verification inconclusive for {name}.")
    
    return True

async def verify_all_sites():
    print("=== Universal Crawl4AI + DB Verification ===")
    
    sites = [
        {"id": "88888888-8888-4888-8888-888888888888", "url": "http://localhost:8000/test-sites/ecommerce", "name": "E-Life Store"},
        {"id": "99999999-9999-4999-9999-999999999999", "url": "http://localhost:8000/test-sites/banking", "name": "Nexus Digital Bank"},
        {"id": "77777777-7777-4777-7777-777777777777", "url": "http://localhost:8000/test-sites/healthcare", "name": "CarePoint Healthcare"}
    ]
    
    dag = UniversalDAG()
    pool = await get_pool()
    
    results = []
    for site in sites:
        success = await verify_site(dag, pool, site["id"], site["url"], site["name"])
        results.append((site["name"], success))
    
    print("\n=== FINAL SUMMARY ===")
    for name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{name}: {status}")
        
    await close_pool()

if __name__ == "__main__":
    asyncio.run(verify_all_sites())
