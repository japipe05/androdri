from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, status
from typing import List, Optional
from app.utils.security import verify_token
from app.services.email_service import EmailService
from app.utils.exceptions import AttachmentTooLargeException, EmailSendException

router = APIRouter(prefix="/email", tags=["email"])

email_service = EmailService()

# Endpoint multipart/form-data to accept files and fields
@router.post("/send")
async def send_email_endpoint(
    asunto: str = Form(...),
    mensaje: str = Form(...),
    comprimir: Optional[bool] = Form(False),
    zip_password: Optional[str] = Form(None),
    files: Optional[List[UploadFile]] = File(None),   # 👈 opcional
    user: str = Depends(verify_token),
):
    """
    Envía correo. Requiere token Bearer en Authorization.
    - asunto (form) -> obligatorio
    - mensaje (form) -> obligatorio
    - comprimir (form) -> opcional boolean
    - zip_password (form) -> opcional string
    - files -> 0..n archivos (multipart)
    """
    # Validaciones
    if not asunto or not mensaje:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="asunto y mensaje son obligatorios"
        )

    attachments = []
    if files:   # 👈 si el cliente no envía nada, files será None
        for fp in files:
            content = await fp.read()
            # Small per-file check (e.g., 10MB per file)
            if len(content) > 10 * 1024 * 1024:
                raise AttachmentTooLargeException(detail=f"Archivo {fp.filename} excede 10MB")
            attachments.append((fp.filename, content))

    try:
        email_service.send_email(
            asunto=asunto,
            mensaje=mensaje,
            attachments=attachments,
            comprimir=comprimir,
            zip_password=zip_password
        )
    except EmailSendException as e:
        raise e

    return {
        "status": "ok",
        "detail": "Correo enviado",
        "archivos": [fp[0] for fp in attachments],
        "comprimido": comprimir,
        "zip_password": bool(zip_password)
    }
