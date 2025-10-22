# app/routers/whatsapp_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.models.message_model import SendMessageRequest, SendMessageResponse
from app.utils.jwt_utils import verify_token
from app.utils.rate_limiter import rate_limit_dependency
from app.services.whatsapp_service import WhatsAppService
from app.config.settings import get_settings

router = APIRouter(prefix="/api/whatsapp", tags=["whatsapp"])
settings = get_settings()
whatsapp_service = WhatsAppService()

@router.post("/send", response_model=SendMessageResponse, status_code=200)
def send_whatsapp(
    payload: SendMessageRequest,
    authorized: str = Depends(verify_token),
    allowed: bool = Depends(rate_limit_dependency)
):
    """
    Envia un mensaje WhatsApp. Requiere Bearer token JWT.
    Rate-limited: máximo 10 requests por 60 segundos por cliente (IP).
    """
    # Basic phone validation (very simple)
    if not payload.phone_number.startswith("+"):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="phone_number must be in E.164 format starting with +")

    success, sid_or_error = whatsapp_service.send_message(payload.phone_number, payload.message)
    if not success:
        raise HTTPException(status_code=500, detail=f"Error sending message: {sid_or_error}")

    return SendMessageResponse(success=True, sid=sid_or_error, detail="Message queued/sent")
