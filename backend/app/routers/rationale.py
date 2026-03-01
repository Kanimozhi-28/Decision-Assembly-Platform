from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from app.db.database import get_pool
from asyncpg import Pool

router = APIRouter(prefix="/rationales", tags=["rationales"])

class RationaleTemplateBase(BaseModel):
    site_id: UUID
    intent: str
    template_text: str

class RationaleTemplate(RationaleTemplateBase):
    id: UUID
    created_at: datetime

@router.get("/{site_id}", response_model=List[RationaleTemplate])
async def list_templates(site_id: UUID, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT * FROM dap.rationale_templates WHERE site_id = $1 ORDER BY created_at DESC",
            site_id
        )
        return [dict(row) for row in rows]

@router.post("/", response_model=RationaleTemplate)
async def create_template(template: RationaleTemplateBase, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            INSERT INTO dap.rationale_templates (site_id, intent, template_text)
            VALUES ($1, $2, $3)
            RETURNING *
            """,
            template.site_id, template.intent, template.template_text
        )
        return dict(row)

@router.delete("/{template_id}")
async def delete_template(template_id: UUID, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        res = await conn.execute("DELETE FROM dap.rationale_templates WHERE id = $1", template_id)
        if res == "DELETE 0":
            raise HTTPException(status_code=404, detail="Template not found")
        return {"status": "deleted"}
