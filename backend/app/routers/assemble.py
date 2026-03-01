from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from app.services.assemble import AssembleService
import uuid

router = APIRouter(prefix="/assemble", tags=["assemble"])

class AssembleRequest(BaseModel):
    site_id: str
    intent: str
    context: Optional[Dict] = None

@router.post("/")
async def assemble(request: AssembleRequest):
    log_path = "assemble_debug_log.txt"
    try:
        try:
            with open(log_path, "a") as f:
                f.write(f"[ROUTER DEBUG] Received request for site: {request.site_id}, intent: {request.intent}\n")
        except:
            pass
        
        # Validate UUID
        try:
            uuid.UUID(request.site_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid site_id UUID")

        service = AssembleService()
        return await service.assemble_experience(
            request.site_id, 
            request.intent, 
            request.context
        )
    except Exception as e:
        import traceback
        error_msg = f"[ROUTER CRITICAL ERROR]: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        try:
            with open(log_path, "a") as f:
                f.write(error_msg + "\n" + "="*50 + "\n")
        except:
            pass
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Router Error: {str(e)}")
