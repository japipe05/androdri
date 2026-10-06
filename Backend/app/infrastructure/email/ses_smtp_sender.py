import asyncio
import logging
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

from app.domain.entities import Email, RenderedEmail
from app.domain.exceptions import EmailDeliveryError, EmailRejectedError

logger = logging.getLogger(__name__)


class SesSmtpEmailSender:
    """Adaptador de salida: envía por el SMTP de Amazon SES (STARTTLS, puerto 587)."""

    def __init__(
        self, host: str, port: int, username: str, password: str, timeout: int = 10
    ) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._timeout = timeout

    async def send(self, email: Email, rendered: RenderedEmail) -> str:
        message, message_id = self._build_message(email, rendered)
        # smtplib es bloqueante: se ejecuta en un hilo para no bloquear el event loop.
        await asyncio.to_thread(self._send_sync, message)
        return message_id

    @staticmethod
    def _build_message(email: Email, rendered: RenderedEmail) -> tuple[EmailMessage, str]:
        message = EmailMessage()
        message_id = make_msgid(domain=email.emisor_domain)
        message["Subject"] = rendered.subject
        message["From"] = email.emisor
        message["To"] = email.receptor
        message["Date"] = formatdate(localtime=False)
        message["Message-ID"] = message_id
        message.set_content(rendered.text)  # texto plano (UTF-8)
        message.add_alternative(rendered.html, subtype="html")  # HTML
        return message, message_id

    def _send_sync(self, message: EmailMessage) -> None:
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(self._host, self._port, timeout=self._timeout) as smtp:
                smtp.ehlo()
                smtp.starttls(context=context)
                smtp.ehlo()
                smtp.login(self._username, self._password)
                smtp.send_message(message)
        except (smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused) as exc:
            logger.warning("SES rechazó emisor/receptor: %s", type(exc).__name__)
            raise EmailRejectedError(
                "El proveedor rechazó el emisor o el receptor "
                "(verifica que el emisor esté verificado en SES y, en sandbox, el receptor también)."
            ) from exc
        except (smtplib.SMTPException, OSError) as exc:
            # Se registra el tipo de error, nunca credenciales ni detalles internos al cliente.
            logger.error("Fallo SMTP: %s", type(exc).__name__)
            raise EmailDeliveryError() from exc
