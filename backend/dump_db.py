import asyncio
import json
from app.db.database import get_pool

async def dump_tables():
    pool = await get_pool()
    async with pool.acquire() as conn:
        print("\n--- SITE CONFIG ---")
        configs = await conn.fetch("SELECT site_id, product_page_rules, trigger_thresholds, allowed_origins FROM dap.site_config")
        for row in configs:
            print(dict(row))
            
        print("\n--- RATIONALE TEMPLATES ---")
        templates = await conn.fetch("SELECT * FROM dap.rationale_templates")
        for row in templates:
            print(dict(row))

if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    asyncio.run(dump_tables())
