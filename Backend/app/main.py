from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.adapters.email.smtp_service import SMTPEmailService
from app.application.usecases.send_contact_email import SendContactEmail
from app.domain.models import ContactForm
from app.config.settings import settings
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


email_service = SMTPEmailService()
usecase = SendContactEmail(email_service)

@app.post("/api/contact")
async def contact(form: ContactForm):
    try:
        usecase.execute(form)
        return {"message": "Mensaje enviado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
