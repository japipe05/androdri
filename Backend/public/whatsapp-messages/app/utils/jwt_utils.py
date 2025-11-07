"""
===============================================================================
Archivo:        jwt_utils.py
Ubicación:      app/utils/jwt_utils.py
Descripción:    Proporciona funciones utilitarias para la generación y 
                verificación de tokens JWT utilizados en la autenticación 
                de la API. Incluye creación de tokens firmados y validación
                de su integridad y vigencia.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0005af
===============================================================================
"""

import time
import jwt
from fastapi import HTTPException, status
from app.config.settings import settings


# --------------------------------------------------------------------------
# Función: create_access_token
# --------------------------------------------------------------------------
def create_access_token(subject: str, expires_in: int | None = None) -> str:
    """
    Genera un **token JWT** firmado con los parámetros definidos en la configuración.

    ### Descripción
    Esta función crea un token JWT que incluye información básica del sujeto
    (por ejemplo, un identificador de cliente o usuario), la fecha de emisión y
    la fecha de expiración. El token se firma utilizando el secreto definido en
    `settings.JWT_SECRET_WHATSAP` y el algoritmo especificado en
    `settings.JWT_ALGORITHM`.

    ### Parámetros
    - **subject** (`str`): Identificador del sujeto o entidad a la que pertenece el token.
    - **expires_in** (`int`, opcional): Tiempo de expiración en segundos.  
      Si no se especifica, se usa el valor por defecto `settings.JWT_EXPIRES_SECONDS`.

    ### Retorna
    - **`str`**: Token JWT firmado (string codificado en Base64).

    ### Ejemplo
    ```python
    token = create_access_token(subject="androdri-client")
    print(token)
    ```

    ### Contenido del payload generado
    ```json
    {
        "sub": "androdri-client",
        "iat": 1718094000,
        "exp": 1718097600,
        "iss": "MiAplicacionAPI"
    }
    ```
    """
    if expires_in is None:
        expires_in = settings.JWT_EXPIRES_SECONDS

    now = int(time.time())
    payload = {
        "sub": subject,              # Sujeto del token
        "iat": now,                  # Fecha de emisión (issued at)
        "exp": now + expires_in,     # Fecha de expiración
        "iss": settings.APP_NAME,    # Emisor del token
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_WHATSAP,
        algorithm=settings.JWT_ALGORITHM
    )
    return token


# --------------------------------------------------------------------------
# Función: verify_token
# --------------------------------------------------------------------------
def verify_token(token: str) -> dict:
    """
    Verifica la validez e integridad de un token JWT.

    ### Descripción
    Decodifica y valida un token JWT utilizando la clave secreta definida en 
    `settings.JWT_SECRET_WHATSAP`. Asegura que el token:
    - No haya expirado.
    - Haya sido firmado con el algoritmo y clave correctos.

    ### Parámetros
    - **token** (`str`): Token JWT a validar (sin el prefijo `Bearer`).

    ### Retorna
    - **`dict`**: El payload decodificado del token (por ejemplo, sub, iat, exp, iss).

    ### Excepciones
    - **401 Unauthorized** → Token expirado (`jwt.ExpiredSignatureError`)
    - **401 Unauthorized** → Token inválido o manipulado (`jwt.InvalidTokenError`)

    ### Ejemplo
    ```python
    try:
        payload = verify_token(token)
        print(payload["sub"])
    except HTTPException as e:
        print(f"Token inválido: {e.detail}")
    ```
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_WHATSAP,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
