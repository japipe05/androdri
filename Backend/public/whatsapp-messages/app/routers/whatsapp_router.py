# app/routers/whatsapp_router.py
from fastapi import APIRouter, Depends, Header, HTTPException, status, Request
from app.models.message_model import WhatsAppMessage
from app.services.whatsapp_service import send_whatsapp_message
from app.utils.jwt_utils import verify_token
from app.utils.rate_limiter import check_rate_limit

router = APIRouter(prefix="/api/whatsapp", tags=["WhatsApp"])

@router.post("/v1")
def send_message(request: Request, data: WhatsAppMessage, authorization: str = Header(...)):
    # Validar token JWT
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.split(" ")[1]
    verify_token(token)

    # Rate Limiting por dirección IP
    client_ip = request.client.host
    check_rate_limit(client_ip)

    # Envío de mensaje
    try:
        response = send_whatsapp_message(data.phone_number, data.message)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
