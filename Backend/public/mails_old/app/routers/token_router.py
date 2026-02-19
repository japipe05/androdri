"""
===============================================================================
Archivo:        token_router.py
Ubicación:      app/routers/token_router.py
Descripción:    Define las rutas de autenticación y generación de tokens JWT.
                Permite emitir tokens de acceso basados en una API Key válida,
                utilizada para autenticar solicitudes hacia otros endpoints
                protegidos de la aplicación.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0007af
===============================================================================
"""

from fastapi import APIRouter, HTTPException
from app.models.token_model import TokenRequest, TokenResponse
from app.utils.jwt_utils import create_access_token
from app.config.settings import settings

# -------------------------------------------------------------------------------
# Definición del router
# -------------------------------------------------------------------------------
router = APIRouter(
    prefix="/api/token-email/v1",
    tags=["Token"]
)


@router.post("/", response_model=TokenResponse, summary="Genera un token JWT válido")
def generate_token(req: TokenRequest):
    """
    Genera un token JWT de acceso.

    Este endpoint valida la API Key proporcionada en el cuerpo de la solicitud.
    Si la clave coincide con la configurada en las variables de entorno,
    se genera un token de acceso JWT firmado con la clave secreta definida en
    la configuración (`settings.JWT_SECRET_KEY`).

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
    -----------
    HTTPException(401)
        Si la API Key es incorrecta o no coincide con la configuración del sistema.

    Retorna
    -------
    TokenResponse
        Objeto con el token JWT generado y el tipo de token (por defecto, "bearer").
    """
    # ---------------------------------------------------------------------------
    # Validación de API Key
    # ---------------------------------------------------------------------------
    if req.api_key != settings.JWT_SECRET_KEY:
        raise HTTPException(status_code=401, detail=f"API Key inválida")

    # ---------------------------------------------------------------------------
    # Generación del token de acceso
    # ---------------------------------------------------------------------------
    token_payload = {"sub": "androdri_user"}
    token = create_access_token(token_payload)

    return TokenResponse(access_token=token)
















