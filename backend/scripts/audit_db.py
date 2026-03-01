
import asyncio
import uuid
import sys
import os

# Add parent directory to sys.path to import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def audit():
    print("Starting Database Audit...")
    try:
        pool = await get_pool()
    except Exception as e:
        print(f"FAILED to connect to DB: {e}")
        return

    async with pool.acquire() as conn:
        # 1. Check Schema
        schema_exists = await conn.fetchval("SELECT EXISTS (SELECT 1 FROM information_schema.schemata WHERE schema_name = 'dap')")
        print(f"Schema 'dap' exists: {schema_exists}")
        
        if not schema_exists:
            print("CRITICAL: 'dap' schema is missing!")
            return

        # 2. Check Tables
        required_tables = ['sites', 'site_config', 'crawl_jobs', 'indexed_pages', 'rationale_templates', 'admin_users']
        existing_tables = await conn.fetch("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dap'")
        existing_table_names = [t['table_name'] for t in existing_tables]
        
        print("\nTable Status:")
        for table in required_tables:
            status = "FOUND" if table in existing_table_names else "MISSING"
            count = 0
            if status == "FOUND":
                count = await conn.fetchval(f"SELECT count(*) FROM dap.{table}")
            print(f" - {table}: {status} ({count} rows)")

        # 3. Check specific data for demo sites
        demo_site_ids = [
            "88888888-8888-4888-8888-888888888888", # E-commerce
            "99999999-9999-4999-9999-999999999999", # Banking
            "77777777-7777-4777-7777-777777777777"  # Healthcare
        ]
        
        print("\nDemo Site Data Audit:")
        for s_id in demo_site_ids:
            site_row = await conn.fetchrow("SELECT name FROM dap.sites WHERE id = $1", uuid.UUID(s_id))
            site_name = site_row['name'] if site_row else "UNKNOWN"
            site_count = 1 if site_row else 0
            
            config_count = await conn.fetchval("SELECT count(*) FROM dap.site_config WHERE site_id = $1", uuid.UUID(s_id))
            pages_count = await conn.fetchval("SELECT count(*) FROM dap.indexed_pages WHERE site_id = $1", uuid.UUID(s_id))
            
            print(f" Site {s_id} ({site_name}):")
            print(f"  - In 'sites': {'YES' if site_count > 0 else 'NO'}")
            print(f"  - In 'site_config': {'YES' if config_count > 0 else 'NO'}")
            print(f"  - In 'indexed_pages': {pages_count} pages")
            
            if config_count > 0:
                config = await conn.fetchrow("SELECT product_page_rules, trigger_thresholds, block_mapping FROM dap.site_config WHERE site_id = $1", uuid.UUID(s_id))
                print(f"  - Product Page Rules: {config['product_page_rules']}")
                print(f"  - Trigger Thresholds: {config['trigger_thresholds']}")
                print(f"  - Block Mapping: {config['block_mapping']}")
            
            rationales = await conn.fetch("SELECT intent, template_text FROM dap.rationale_templates WHERE site_id = $1", uuid.UUID(s_id))
            print(f"  - Rationale Templates count: {len(rationales)}")
            for r in rationales[:2]: # Show first 2
                print(f"    - {r['intent']}: {r['template_text'][:60]}...")

if __name__ == "__main__":
    asyncio.run(audit())
