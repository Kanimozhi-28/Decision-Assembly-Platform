from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import Settings
import os
from pathlib import Path

from app.routers import crawl, search, admin, auth, rationale, assemble, behavior

app = FastAPI(title="DAP Backend", version="1.0.0")
settings = Settings()

# Mount SDK dist folder to serve loader.js and dap-sdk.js
sdk_dist_path = Path(__file__).resolve().parent.parent.parent / "sdk" / "dist"
if sdk_dist_path.exists():
    app.mount("/sdk", StaticFiles(directory=str(sdk_dist_path)), name="sdk")

# Mount test-sites folder for demo access
test_sites_path = Path(__file__).resolve().parent.parent.parent / "test-sites"
if test_sites_path.exists():
    app.mount("/test-sites", StaticFiles(directory=str(test_sites_path)), name="test-sites")

app.include_router(auth.router)
app.include_router(rationale.router)
app.include_router(crawl.router)
app.include_router(search.router)
app.include_router(admin.router)
app.include_router(assemble.router)
app.include_router(behavior.router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("[STARTUP] Initializing database pool...")
    from app.db.database import get_pool
    await get_pool()
    print("[STARTUP] Database pool initialized.")

@app.on_event("shutdown")
async def shutdown():
    from app.db.database import close_pool
    await close_pool()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/test-db")
async def test_db():
    from app.db.database import get_pool
    pool = await get_pool()
    async with pool.acquire() as conn:
        result = await conn.fetchval("SELECT 1")
    return {"status": "ok", "db_result": result}
