"""
===============================================================================
Archivo:        whatsapp_router.py
Ubicación:      app/routers/whatsapp_router.py
Descripción:    Define los endpoints relacionados con el envío de mensajes de 
                WhatsApp. Incluye validación mediante token JWT, control de 
                frecuencia (rate limiting) y encapsula la lógica de envío 
                utilizando el servicio whatsapp_service.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0003af
===============================================================================
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
    Security
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models.whatsapp_model import WhatsAppSendRequest
from app.utils.jwt_utils import verify_token
from app.services.whatsapp_service import whatsapp_service
from app.utils.rate_limiter import check_rate_limit

# --------------------------------------------------------------------------
# Router de envío de mensajes WhatsApp
# --------------------------------------------------------------------------
router = APIRouter(
    prefix="/api/whatsapp/v1",
    tags=["whatsapp"],
    responses={
        200: {"description": "Mensaje enviado exitosamente"},
        401: {"description": "No autorizado - Token inválido o ausente"},
        429: {"description": "Límite de solicitudes excedido"}
    }
)

# --------------------------------------------------------------------------
# Configuración del esquema Bearer (para documentación interactiva Swagger)
# --------------------------------------------------------------------------
bearer_scheme = HTTPBearer()


# --------------------------------------------------------------------------
# Dependencia para validar el token JWT incluido en la cabecera Authorization
# --------------------------------------------------------------------------
async def jwt_bearer(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    """
    Valida el token JWT enviado en la cabecera `Authorization`.

    ### Flujo:
    1. Verifica la presencia del encabezado `Authorization: Bearer <token>`.
    2. Extrae el token y lo valida mediante `verify_token`.
    3. Si el token no es válido o ha expirado, genera un error 401.

    ### Parámetros:
    - **credentials**: Objeto proporcionado por FastAPI que contiene las credenciales HTTP.

    ### Retorna:
    - Datos decodificados del token JWT (dict).

    ### Errores:
    - **401 Unauthorized**: Si no se proporciona token o es inválido.
    """
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header"
        )

    token = credentials.credentials  # Obtiene el token sin el prefijo 'Bearer '
    return verify_token(token)


# --------------------------------------------------------------------------
# Endpoint principal: envío de mensajes de WhatsApp
# --------------------------------------------------------------------------
@router.post(
    "/",
    summary="Enviar mensaje de WhatsApp",
    response_description="Resultado del envío del mensaje"
)
async def send_whatsapp(
    payload: WhatsAppSendRequest,
    request: Request,
    _payload=Depends(jwt_bearer)
):
    """
    Envía un mensaje de WhatsApp al número especificado.

    ### Descripción
    Este endpoint permite enviar un mensaje de WhatsApp a través del servicio
    configurado. Para acceder, el cliente debe autenticarse mediante un **token JWT**
    válido (usualmente obtenido desde `/api/token-whatsapp/v1`).

    Además, aplica un control de **rate limiting** para evitar abusos:
    máximo **10 solicitudes por IP cada 60 segundos**.

    ### Parámetros
    - **payload** (`WhatsAppSendRequest`): Contiene el número de teléfono y mensaje.
    - **request** (`Request`): Usado para determinar la IP del cliente en el control de tasa.
    - **_payload**: Datos decodificados del JWT (proporcionados automáticamente por la dependencia).

    ### Ejemplo de solicitud
    ```json
    {
        "phone_number": "+573001234567",
        "message": "Hola, este es un mensaje de prueba!"
    }
    ```

    ### Encabezado requerido
    ```
    Authorization: Bearer <token_jwt_válido>
    ```

    ### Ejemplo de respuesta exitosa
    ```json
    {
        "ok": true,
        "result": {
            "message_id": "abc123",
            "status": "SENT"
        }
    }
    ```

    ### Errores posibles
    - **401 Unauthorized**: Token inválido o ausente.
    - **429 Too Many Requests**: Si se excede el límite de solicitudes por minuto.
    - **500 Internal Server Error**: Si ocurre un error interno durante el envío.

    ### Seguridad
    - Autenticación vía **JWT Bearer Token**.
    - Protección anti-spam mediante **rate limiting**.
    """
    # Control de rate limit (máx. 10 solicitudes / 60 segundos por IP)
    check_rate_limit(request)

    # Lógica de envío del mensaje (delegada al servicio)
    result = whatsapp_service.send_message(
        to=payload.phone_number,
        body=payload.message
    )

    return {"ok": True, "result": result}
