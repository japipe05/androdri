import smtplib
from email.mime.text import MIMEText
from app.config.settings import settings

def send_email(subject: str, body: str, sender_email: str):
    """
    Envía un correo usando SMTP con TLS.
    """
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = settings.RECEIVER_EMAIL

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(sender_email, settings.RECEIVER_EMAIL, msg.as_string())
