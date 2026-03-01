from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class CrawlJobBase(BaseModel):
    site_id: UUID
    status: str

class CrawlJobCreate(CrawlJobBase):
    pass

class CrawlJob(CrawlJobBase):
    id: UUID
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    last_synced_at: Optional[datetime] = None
    error_message: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
