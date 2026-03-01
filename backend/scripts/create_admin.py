import sys
from pathlib import Path

# Add backend dir to path BEFORE other imports
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import asyncio
import asyncpg
from passlib.context import CryptContext
from app.config import Settings

settings = Settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(email, password):
    hashed_password = pwd_context.hash(password)
    
    try:
        conn = await asyncpg.connect(settings.database_url)
        await conn.execute(
            "INSERT INTO dap.admin_users (email, password_hash) VALUES ($1, $2) ON CONFLICT (email) DO UPDATE SET password_hash = $2",
            email, hashed_password
        )
        print(f"SUCCESS: Admin user {email} created/updated.")
        await conn.close()
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    email = "admin@example.com"
    password = "adminpassword123"
    
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(create_user(email, password))
