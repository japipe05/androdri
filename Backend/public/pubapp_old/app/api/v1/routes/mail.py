from fastapi import APIRouter, HTTPException
from app.schemas.mail import ContactMail
from app.services.email_service import send_contact_email

router = APIRouter()

@router.post("/contact")
async def contact_mail(data: ContactMail):
    try:
        await send_contact_email(data.dict())
        return {
            "success": True,
            "message": "Correo enviado correctamente"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
