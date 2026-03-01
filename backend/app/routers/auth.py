from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from app.config import Settings
from app.db.database import get_pool
from asyncpg import Pool
import uuid

router = APIRouter(prefix="/auth", tags=["auth"])
settings = Settings()

def get_pwd_context():
    from passlib.context import CryptContext
    return CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    from jose import jwt
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), pool: Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT id, email, password_hash FROM dap.admin_users WHERE email = $1", form_data.username)
        
        pwd_context = get_pwd_context()
        if not row or not pwd_context.verify(form_data.password, row['password_hash']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        access_token = create_access_token(data={"sub": str(row['id']), "email": row['email']})
        return {"access_token": access_token, "token_type": "bearer"}
