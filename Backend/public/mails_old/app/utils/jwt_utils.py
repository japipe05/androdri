"""
===============================================================================
Archivo:        jwt_utils.py
Ubicación:      app/utils/jwt_utils.py
Descripción:    Utilidades para la creación y validación de tokens JWT.
                Incluye funciones para generar tokens de acceso con expiración
                y verificar su validez, utilizando las claves definidas en la
                configuración global (`settings.py`).
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0009af
===============================================================================
"""

import jwt
from datetime import datetime, timedelta
from app.config.settings import settings


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    """
    Genera un token JWT firmado con la clave secreta de configuración.

    Parámetros
    ----------
    data : dict
        Diccionario con los datos (claims) que se incluirán en el payload del token.
    expires_delta : timedelta, opcional
        Tiempo de expiración del token. Por defecto, 1 hora.

    Retorna
    -------
    str
        Token JWT firmado y codificado.

    Ejemplo
    -------
    >>> token = create_access_token({"sub": "androdri_user"})
    >>> print(token)
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm="HS256"
    )
    return token


def verify_token(token: str) -> dict | None:
    """
    Verifica la validez y firma de un token JWT.

    Parámetros
    ----------
    token : str
        Token JWT a validar.

    Retorna
    -------
    dict | None
        Payload decodificado si el token es válido. `None` si ha expirado o es inválido.

    Excepciones controladas
    -----------------------
    jwt.ExpiredSignatureError
        Se lanza si el token ha expirado (en cuyo caso se devuelve `None`).

    Ejemplo
    -------
    >>> payload = verify_token(token)
    >>> if payload:
    ...     print(payload["sub"])
    ... else:
    ...     print("Token inválido o expirado")
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
