from fastapi import APIRouter
import jwt
from datetime import datetime, timedelta
from app.config.settings import settings

router = APIRouter(prefix="/api/token", tags=["auth"])

@router.get("/")
def generate_token():
    """
    Genera un token JWT válido (por 2 horas) para pruebas.
    """
    payload = {
        "sub": "androdri",
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")
    return {"token": token}
