from email.message import EmailMessage
import smtplib
from app.config.settings import settings
from app.domain.models import ContactForm
from app.ports.email_port import EmailPort


class SMTPEmailService(EmailPort):
    def send(self, contact: ContactForm) -> None:
        msg = EmailMessage()
        msg["Subject"] = f"Nuevo mensaje de contacto: {contact.name}"
        msg["From"] = settings.SMTP_USER
        msg["To"] = settings.RECEIVER_EMAIL
        msg.set_content(
            f"Nombre: {contact.name}\nCorreo: {contact.email}\n\nMensaje:\n{contact.message}"
        )

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
