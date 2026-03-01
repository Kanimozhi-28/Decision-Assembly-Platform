import asyncio
import asyncpg
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from app.config import Settings

async def fix_config():
    settings = Settings()
    try:
        conn = await asyncpg.connect(settings.database_url)
        # Update specifically for our known site ID
        site_id = 'f203f546-e89b-48da-8007-0653a57debab'
        await conn.execute(
            "UPDATE dap.site_config SET product_page_rules = $1 WHERE site_id = $2",
            '{"url_patterns": ["product-"]}', site_id
        )
        print("SUCCESS: Config updated with product recognition rules.")
        await conn.close()
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(fix_config())
