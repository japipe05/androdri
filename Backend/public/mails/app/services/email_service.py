import smtplib
from email.message import EmailMessage
from app.config.settings import settings
from app.utils.compress_utils import compress_files
#from app.utils.compress_utils import compress_files_7z as compress_files

from typing import List

def send_email(asunto: str, mensaje: str, archivos: List = None, comprimir=False, password=None):
    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = settings.SMTP_USER
    msg["To"] = settings.SMTP_USER  # Puedes cambiar por un destinatario dinámico
    msg.set_content(mensaje)

    if archivos:
        if comprimir:
            zip_path = compress_files(archivos, password)
            with open(zip_path, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="zip", filename="archivos.zip")
        else:
            for file in archivos:
                file.file.seek(0)
                msg.add_attachment(file.file.read(),
                                   maintype="application",
                                   subtype="octet-stream",
                                   filename=file.filename)

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        smtp.send_message(msg)

    return {"message": "Correo enviado exitosamente ✅"}
