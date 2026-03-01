from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SiteBase(BaseModel):
    name: str
    base_url: str

class SiteCreate(SiteBase):
    pass

class Site(SiteBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
