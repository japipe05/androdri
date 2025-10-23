# ------------------------
# File: app/routers/whatsapp_router.py
# ------------------------
from fastapi import APIRouter, Depends, HTTPException, status, Request, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models.whatsapp_model import WhatsAppSendRequest
from app.utils.jwt_utils import verify_token
from app.services.whatsapp_service import whatsapp_service
from app.utils.rate_limiter import check_rate_limit

router = APIRouter(prefix="/api/whatsapp/v1", tags=["whatsapp"])

# Configuración del esquema Bearer para Swagger (OpenAPI)
bearer_scheme = HTTPBearer()

# Dependencia para validar JWT
async def jwt_bearer(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    if not credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")

    token = credentials.credentials  # Obtiene el token sin el prefijo 'Bearer '
    return verify_token(token)

# Endpoint principal
@router.post("/send")
async def send_whatsapp(payload: WhatsAppSendRequest, request: Request, _payload=Depends(jwt_bearer)):
    # Control de rate limit (máx. 10 solicitudes / 60 segundos por IP)
    check_rate_limit(request)

    # Lógica de envío del mensaje
    result = whatsapp_service.send_message(to=payload.phone_number, body=payload.message)
    return {"ok": True, "result": result}
