from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth")


@router.post("/register" , tags=["Auth"], summary="Información general y documentación de la API")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):

    return AuthService.register(db, username, email, password)


@router.post("/login", tags=["Auth"], summary="Información general y documentación de la API")
def login(username: str, password: str, db: Session = Depends(get_db)):

    token = AuthService.login(db, username, password)

    return {"access_token": token}


@router.post("/change-password", tags=["Auth"], summary="Información general y documentación de la API")
def change_password(username: str, new_password: str, db: Session = Depends(get_db)):

    AuthService.change_password(db, username, new_password)

    return {"message": "password updated"}