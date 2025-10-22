# app/utils/jwt_utils.py
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from app.config.settings import get_settings

settings = get_settings()

# Declarar esquema estándar de seguridad con formato JWT
jwt_bearer_scheme = HTTPBearer(
    bearerFormat="JWT",
    auto_error=False,
)

def create_access_token(subject: str, expires_delta: int = None) -> str:
    """Genera un JWT firmado."""
    if expires_delta is None:
        expires_delta = settings.JWT_EXP_SECONDS
    now = datetime.utcnow()
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(seconds=expires_delta),
    }
    return jwt.encode(payload, settings.JWT_SECRET_WHATSAP, algorithm=settings.JWT_ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Security(jwt_bearer_scheme)) -> str:
    """Valida el token JWT obtenido desde 'Authorization: Bearer <token>'."""
    if credentials is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Missing authorization credentials")
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid authorization scheme")

    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_WHATSAP, algorithms=[settings.JWT_ALGORITHM])
        subject = payload.get("sub")
        if not subject:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token missing subject")
        return subject
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid token")
