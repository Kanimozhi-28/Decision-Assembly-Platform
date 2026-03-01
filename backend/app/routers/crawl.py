from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.services.indexing import IndexingService
import uuid

router = APIRouter(prefix="/crawl", tags=["crawl"])

class CrawlRequest(BaseModel):
    url: str
    site_id: str

from app.services.dag import UniversalDAG

async def run_universal_crawl(url: str, site_id: str):
    dag = UniversalDAG()
    await dag.run_discovery(url, site_id)
    # Automatically trigger Phase 2: Catalog Sync
    await dag.sync_catalog(site_id, url)

@router.post("/universal")
async def trigger_universal_crawl(request: CrawlRequest, background_tasks: BackgroundTasks):
    try:
        uuid.UUID(request.site_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid site_id UUID")

    background_tasks.add_task(run_universal_crawl, request.url, request.site_id)
    
    return {"status": "accepted", "message": f"Universal discovery for {request.url} started"}
