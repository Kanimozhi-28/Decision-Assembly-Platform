
import asyncio
import uuid
import sys
import os
import json

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import get_pool

async def harden_db():
    print("Hardening Database Configuration...")
    pool = await get_pool()
    
    block_mapping = {
        "help_me_choose": ["shortlist", "recommendation", "trade-off", "action"],
        "compare_options": ["comparison", "costs", "benefits", "limitations"],
        "check_eligibility": ["eligibility", "use-case-fit", "action"],
        "understand_differences": ["comparison", "trade-off", "examples"],
        "just_exploring": ["shortlist", "benefits", "custom-query"]
    }
    
    demo_site_ids = [
        "88888888-8888-4888-8888-888888888888",
        "99999999-9999-4999-9999-999999999999",
        "77777777-7777-4777-7777-777777777777"
    ]
    
    async with pool.acquire() as conn:
        for s_id in demo_site_ids:
            print(f"Updating site_config for: {s_id}")
            await conn.execute(
                "UPDATE dap.site_config SET block_mapping = $1 WHERE site_id = $2",
                json.dumps(block_mapping),
                uuid.UUID(s_id)
            )
    print("Database Hardening Complete.")

if __name__ == "__main__":
    asyncio.run(harden_db())
