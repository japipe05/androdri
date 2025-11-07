"""
===============================================================================
Archivo:        token_router.py
Ubicación:      app/routers/token_router.py
Descripción:    Define el endpoint encargado de emitir un token JWT para clientes
                autorizados (por ejemplo, integraciones con WhatsApp). Valida la 
                clave API proporcionada por el cliente y genera un token de acceso 
                temporal utilizando las utilidades de JWT.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0002af
===============================================================================
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.models.token_model import TokenRequest, TokenResponse
from app.utils.jwt_utils import create_access_token
from app.config.settings import settings

# --------------------------------------------------------------------------
# Router de emisión de tokens JWT para clientes autorizados
# --------------------------------------------------------------------------
router = APIRouter(
    prefix="/api/token-whatsapp/v1",
    tags=["token-whatsapp"],
    responses={
        401: {"description": "No autorizado - API key inválida"},
        200: {"description": "Token JWT emitido exitosamente"}
    }
)


@router.post(
    "/",
    response_model=TokenResponse,
    summary="Emitir token JWT para cliente autorizado",
    response_description="Devuelve un token de acceso válido"
)
async def issue_token(payload: TokenRequest):
    """
    Genera un **token JWT** para clientes que presenten la clave API correcta.

    ### Descripción
    Este endpoint valida que el cliente envíe la `api_key` configurada en
    las variables de entorno del sistema (`settings.JWT_SECRET_WHATSAP`).
    Si la validación es exitosa, se genera y devuelve un **token JWT** 
    firmado, el cual puede ser utilizado para autenticar futuras solicitudes.

    ### Parámetros de entrada
    - **payload** (`TokenRequest`): Objeto JSON que contiene la `api_key`
      del cliente solicitante.

    ### Respuestas
    - **200 OK** → Retorna un objeto `TokenResponse` con el token generado.
    - **401 Unauthorized** → Si la `api_key` no coincide con la esperada.

    ### Ejemplo de solicitud
    ```json
    {
        "api_key": "my-secret-key"
    }
    ```

    ### Ejemplo de respuesta exitosa
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6..."
    }
    ```

    ### Seguridad
    ⚠️ En un entorno real, se recomienda:
    - Utilizar un registro de clientes autorizado (en lugar de una sola clave compartida)
    - Establecer tiempo de expiración corto para los tokens
    - Implementar rotación de claves y autenticación basada en roles
    """
    # Validación simple: el cliente debe presentar la api_key configurada
    if payload.api_key != settings.JWT_SECRET_WHATSAP:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api_key"
        )

    # Genera el token JWT firmado
    token = create_access_token(subject="androdri-client")

    # Retorna el token dentro del modelo de respuesta
    return TokenResponse(access_token=token)
