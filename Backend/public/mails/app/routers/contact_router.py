from fastapi import APIRouter, UploadFile, File, Form, Depends
from typing import List, Optional
from app.models.email_model import EmailRequest
from app.services.email_service import send_email
from app.utils.jwt_utils import verify_token

router = APIRouter(prefix="/api/contact/v1", tags=["Contact"])

@router.post("/", dependencies=[Depends(verify_token)])
async def enviar_correo(
    asunto: str = Form(...),
    mensaje: str = Form(...),
    comprimir: Optional[bool] = Form(False),
    password: Optional[str] = Form(None),
    archivos: Optional[List[UploadFile]] = File(None)
):
    response = send_email(asunto, mensaje, archivos, comprimir, password)
    return response
