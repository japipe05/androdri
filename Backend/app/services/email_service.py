import smtplib
from email.message import EmailMessage
from typing import List, Tuple, Optional
from app.config.settings import settings
from app.utils.exceptions import EmailSendException
import mimetypes
from app.utils.compress import create_zip

MAX_TOTAL_ATTACHMENT_SIZE = 20 * 1024 * 1024  # 20 MB total


class EmailService:
    def __init__(self):
        self.smtp_host = settings.SMTP_HOST
        self.smtp_port = settings.SMTP_PORT
        self.smtp_user = settings.SMTP_USER
        self.smtp_pass = settings.SMTP_PASSWORD

    def _attach_files(self, msg: EmailMessage, files: List[Tuple[str, bytes]]) -> None:
        """Adjuntar archivos normales uno por uno"""
        for filename, content in files:
            ctype, encoding = mimetypes.guess_type(filename)
            if ctype is None:
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/", 1)
            msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=filename)

    def _check_total_size(self, files: List[Tuple[str, bytes]]):
        """Valida que el total de archivos no supere el límite"""
        total = sum(len(content) for _, content in files)
        if total > MAX_TOTAL_ATTACHMENT_SIZE:
            raise EmailSendException(
                detail=f"Total adjuntos excede el máximo permitido ({MAX_TOTAL_ATTACHMENT_SIZE // (1024*1024)} MB)"
            )

    def send_email(
        self,
        asunto: str,
        mensaje: str,
        attachments: Optional[List[Tuple[str, bytes]]] = None,
        comprimir: bool = False,
        zip_password: Optional[str] = None,
        to_email: Optional[str] = None,
    ) -> None:
        """
        Envía un correo electrónico.
        - attachments: lista de tuplas (filename, bytes)
        - comprimir: si es True, los adjuntos se comprimen en un ZIP
        - zip_password: opcional, protege el ZIP si se envía
        """
        attachments = attachments or []
        self._check_total_size(attachments)

        msg = EmailMessage()
        msg["Subject"] = asunto
        msg["From"] = self.smtp_user
        msg["To"] = to_email or self.smtp_user
        msg.set_content(mensaje)

        if attachments and comprimir:
            # Crear ZIP (con o sin contraseña)
            zip_bytes = create_zip(attachments, password=zip_password)
            #zip_bytes = create_zip(attachments, password=zip_password, encryption="zipcrypto")

            msg.add_attachment(
                zip_bytes,
                maintype="application",
                subtype="zip",
                filename="attachments.zip"
            )
        elif attachments:
            # Adjuntar archivos tal cual
            self._attach_files(msg, attachments)

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.send_message(msg)
        except Exception as exc:
            raise EmailSendException(detail=f"No se pudo enviar el correo: {exc}") from exc
