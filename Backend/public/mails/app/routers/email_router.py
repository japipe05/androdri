"""
===============================================================================
Archivo:        email_router.py
Ubicación:      app/routers/email_router.py
Descripción:    Define los endpoints relacionados con el envío de correos
                electrónicos dentro de la API. Implementa validación de token
                JWT, control de tasa (rate limiting) y manejo de archivos
                adjuntos opcionales.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0005af
===============================================================================
"""

from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
    Form,
    HTTPException,
    status
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List, Optional
from app.utils.jwt_utils import verify_token
from app.utils.rate_limiter import rate_limiter
from app.services.email_service import EmailService


# ------------------------------------------------------------------------------
# Configuración de seguridad y enrutamiento
# ------------------------------------------------------------------------------
security = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix="/api/email/v1",
    tags=["Email"],
    responses={
        200: {"description": "Correo enviado exitosamente"},
        401: {"description": "Token JWT inválido o expirado"},
        429: {"description": "Límite de envíos excedido"},
        500: {"description": "Error interno al enviar el correo"}
    }
)


# ------------------------------------------------------------------------------
# Endpoint principal: Envío de correos electrónicos
# ------------------------------------------------------------------------------
@router.post(
    "/",
    summary="Enviar correo electrónico",
    response_description="Resultado del envío del correo electrónico"
)
async def send_email(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    asunto: str = Form(..., description="Asunto o título del correo electrónico."),
    mensaje: str = Form(..., description="Cuerpo o contenido principal del correo."),
    comprimir: bool = Form(False, description="Indica si los archivos adjuntos deben comprimirse antes del envío."),
    password: Optional[str] = Form(None, description="Contraseña opcional para proteger el archivo comprimido."),
    archivos: Optional[List[UploadFile]] = File(None, description="Lista de archivos adjuntos opcionales.")
):
    """
    Envía un correo electrónico con o sin archivos adjuntos.

    Este endpoint permite enviar correos electrónicos autenticados mediante 
    un **token JWT válido** (enviado en el encabezado `Authorization` del tipo 
    `Bearer`). También ofrece la opción de comprimir archivos adjuntos y 
    protegerlos con contraseña.

    Además, aplica **control de tasa (Rate Limiting)** para restringir cada 
    usuario a un máximo de **10 envíos por hora**, evitando el abuso del servicio.

    ---
    ### 🔐 Requisitos de seguridad
    - Autenticación mediante **Bearer Token JWT**.
    - El token debe ser generado previamente usando el endpoint:
      `/api/token-email/v1`.

    ---
    ### 📥 Parámetros del formulario (multipart/form-data)

    | Parámetro  | Tipo | Requerido | Descripción |
    |-------------|------|------------|--------------|
    | `asunto`    | `str` | ✅ | Asunto o título del correo electrónico. |
    | `mensaje`   | `str` | ✅ | Cuerpo o contenido principal del correo. |
    | `comprimir` | `bool` | ❌ | Si es `True`, los archivos adjuntos se comprimen antes del envío. |
    | `password`  | `str` | ❌ | Contraseña opcional para proteger el archivo comprimido (si aplica). |
    | `archivos`  | `List[UploadFile]` | ❌ | Lista de archivos adjuntos opcionales. |

    ---
    ### 🧠 Lógica interna

    1. **Validación del token JWT**:  
       Se extrae desde el encabezado `Authorization` y se valida su integridad.  
       Si el token es inválido o ha expirado → se lanza un error `401 Unauthorized`.

    2. **Control de tasa (Rate Limiter)**:  
       Cada usuario identificado por su `sub` en el token tiene un límite de  
       10 correos por hora. Si se supera → se lanza un error `429 Too Many Requests`.

    3. **Envío del correo**:  
       Se crea una instancia del servicio `EmailService`, que maneja la composición  
       y el envío del mensaje (HTML + adjuntos).

    ---
    ### 🧾 Ejemplo de solicitud (cURL)

    ```bash
    curl -X POST "https://api.tuapp.com/api/email/v1/" \
    -H "Authorization: Bearer <token_jwt_valido>" \
    -F "asunto=Reporte semanal" \
    -F "mensaje=Adjunto el reporte correspondiente." \
    -F "comprimir=true" \
    -F "password=1234" \
    -F "archivos=@/ruta/a/archivo1.pdf"
    ```

    ---
    ### 🔁 Respuestas posibles

    **200 OK**
    ```json
    {
        "message": "Correo enviado correctamente"
    }
    ```

    **401 Unauthorized**
    ```json
    {
        "detail": "Token inválido o expirado"
    }
    ```

    **429 Too Many Requests**
    ```json
    {
        "detail": "Límite de 10 envíos alcanzado. Intente más tarde."
    }
    ```

    ---
    Retorna
    -------
    dict
        Un mensaje de confirmación indicando que el correo fue enviado exitosamente.
    """
    # --------------------------------------------------------------------------
    # 1️⃣ Validación del token JWT
    # --------------------------------------------------------------------------
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Encabezado Authorization ausente o malformado."
        )

    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    # --------------------------------------------------------------------------
    # 2️⃣ Control de tasa por usuario
    # --------------------------------------------------------------------------
    user_id = payload.get("sub")
    if not rate_limiter.is_allowed(user_id):
        raise HTTPException(
            status_code=429,
            detail="Límite de 10 envíos alcanzado. Intente más tarde."
        )

    # --------------------------------------------------------------------------
    # 3️⃣ Envío del correo electrónico
    # --------------------------------------------------------------------------
    try:
        service = EmailService()
        service.send_email(asunto, mensaje, archivos, comprimir, password)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al enviar el correo: {str(e)}"
        )

    return {"message": "Correo enviado correctamente"}
