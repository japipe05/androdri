
# ------------------------
# File: app/utils/jwt_utils.py
# ------------------------
import time
import jwt
from fastapi import HTTPException, status
from app.config.settings import settings

def create_access_token(subject: str, expires_in: int | None = None) -> str:
    if expires_in is None:
        expires_in = settings.JWT_EXPIRES_SECONDS
    now = int(time.time())
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + expires_in,
        "iss": settings.APP_NAME,
    }
    token = jwt.encode(payload, settings.JWT_SECRET_WHATSAP, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_WHATSAP, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
