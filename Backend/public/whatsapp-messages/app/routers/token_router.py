
# ------------------------
# File: app/routers/token_router.py
# ------------------------
from fastapi import APIRouter, Depends
from app.models.token_model import TokenRequest, TokenResponse
from app.utils.jwt_utils import create_access_token
from app.config.settings import settings

router = APIRouter(prefix="/api/token-whatsapp/v1", tags=["token-whatsapp"])

@router.post("/", response_model=TokenResponse)
async def issue_token(payload: TokenRequest):
    # Simple authentication: client must present the configured api key
    if payload.api_key != settings.JWT_SECRET_WHATSAP:
        # In a real system use a different shared secret or client registry
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid api_key")

    token = create_access_token(subject="androdri-client")
    return TokenResponse(access_token=token)
