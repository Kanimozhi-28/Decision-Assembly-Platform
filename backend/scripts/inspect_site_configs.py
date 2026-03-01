import asyncio
import json
import uuid
import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def inspect():
    pool = await get_pool()
    demo_site_ids = [
        "88888888-8888-4888-8888-888888888888", # E-commerce
        "99999999-9999-4999-9999-999999999999", # Banking
        "77777777-7777-4777-7777-777777777777"  # Healthcare
    ]
    
    async with pool.acquire() as conn:
        for s_id in demo_site_ids:
            row = await conn.fetchrow("SELECT product_page_rules FROM dap.site_config WHERE site_id = $1", uuid.UUID(s_id))
            if row:
                print(f"SITE ID: {s_id}")
                print(f"RULES: {json.dumps(row['product_page_rules'], indent=2)}")
                print("-" * 20)
            else:
                print(f"SITE {s_id} NOT FOUND")

if __name__ == "__main__":
    asyncio.run(inspect())
