from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.site import Site, SiteCreate
from app.schemas.config import SiteConfig
from app.db.database import get_pool
from asyncpg import Pool
import uuid
import json

router = APIRouter(prefix="/sites", tags=["admin"])

@router.get("/", response_model=List[Site])
async def list_sites(pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM dap.sites ORDER BY created_at DESC")
        return [dict(row) for row in rows]

@router.post("/", response_model=Site)
async def create_site(site: SiteCreate, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        # Create Site
        site_id = uuid.uuid4()
        row = await conn.fetchrow(
            """
            INSERT INTO dap.sites (id, name, base_url)
            VALUES ($1, $2, $3)
            RETURNING *
            """,
            site_id, site.name, site.base_url
        )
        
        # Create default Site Config
        await conn.execute(
            """
            INSERT INTO dap.site_config (site_id) VALUES ($1)
            """,
            site_id
        )
        
        return dict(row)

@router.get("/{site_id}", response_model=Site)
async def get_site(site_id: uuid.UUID, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM dap.sites WHERE id = $1", site_id)
        if not row:
            raise HTTPException(status_code=404, detail="Site not found")
        return dict(row)

@router.get("/{site_id}/config")
async def get_site_config(site_id: uuid.UUID, pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            SELECT c.*, s.name as site_name 
            FROM dap.site_config c 
            JOIN dap.sites s ON c.site_id = s.id 
            WHERE c.site_id = $1
            """, 
            site_id
        )
        if not row:
            raise HTTPException(status_code=404, detail="Config not found")
        
        data = dict(row)
        # asyncpg handles JSONB well, but let's ensure it's a dict for the response
        for field in ['product_page_rules', 'trigger_thresholds', 'block_mapping', 'white_label', 'excluded_url_patterns', 'allowed_origins']:
            if data.get(field) and isinstance(data[field], str):
                data[field] = json.loads(data[field])
        return data

@router.patch("/{site_id}/config")
async def update_site_config(site_id: uuid.UUID, config_update: dict, pool: Pool = Depends(get_pool)):
    """
    Updates site configuration. Field-by-field update.
    """
    async with pool.acquire() as conn:
        # Check if exists
        row = await conn.fetchrow("SELECT site_id FROM dap.site_config WHERE site_id = $1", site_id)
        if not row:
            raise HTTPException(status_code=404, detail="Config not found")

        # Dynamic update query
        fields = []
        values = [site_id]
        
        allowed_fields = [
            'product_page_rules', 'cta_selectors', 'help_me_choose_selector',
            'trigger_thresholds', 'commentary_templates', 'block_mapping',
            'white_label', 'excluded_url_patterns', 'allowed_origins',
            'session_timeout_min', 'restoration_window_min'
        ]

        for i, (key, value) in enumerate(config_update.items()):
            if key in allowed_fields:
                fields.append(f"{key} = ${len(values) + 1}")
                # If it's a dict/list, asyncpg will handle it as JSONB automatically
                values.append(value)
        
        if not fields:
             raise HTTPException(status_code=400, detail="No valid fields provided")

        query = f"""
            UPDATE dap.site_config 
            SET {', '.join(fields)}, updated_at = now() 
            WHERE site_id = $1
            RETURNING *
        """
        
        updated_row = await conn.fetchrow(query, *values)
        return dict(updated_row)
