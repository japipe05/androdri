from fastapi import APIRouter, Depends, HTTPException, status
from app.models.schemas import TokenRequest, TokenResponse
from app.config.settings import settings
from app.utils.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=TokenResponse)
def login_for_token(form: TokenRequest):
    # En un sistema real: validar contra base de datos con hashing
    if form.username != settings.ADMIN_USER or form.password != settings.ADMIN_PASS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario/contraseña incorrectos")
    token = create_access_token(subject=form.username)
    return {"access_token": token}
