import asyncio
from app.db.database import get_pool

async def check_configs():
    site_ids = [
        '99999999-9999-4999-9999-999999999999', # Banking
        '88888888-8888-4888-8888-888888888888', # Ecommerce
        '77777777-7777-4777-7777-777777777777'  # Healthcare
    ]
    pool = await get_pool()
    async with pool.acquire() as conn:
        for sid in site_ids:
            print(f"\n--- CONFIG FOR {sid} ---")
            row = await conn.fetchrow("SELECT site_id, product_page_rules, trigger_thresholds, allowed_origins FROM dap.site_config WHERE site_id = $1", sid)
            if row:
                print(dict(row))
            else:
                print("NOT FOUND")

if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    asyncio.run(check_configs())
