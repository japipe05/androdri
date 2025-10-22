# app/services/whatsapp_service.py
from twilio.rest import Client
from app.config.settings import get_settings
from typing import Tuple
import logging

settings = get_settings()
logger = logging.getLogger("whatsapp_service")

class WhatsAppService:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.from_number = f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}"

    def send_message(self, to_number: str, body: str) -> Tuple[bool, str]:
        """
        Sends a WhatsApp message via Twilio and returns (success, sid_or_error)
        """
        try:
            # Twilio expects 'whatsapp:+123...' for to/from
            to = to_number if to_number.startswith("whatsapp:") else f"whatsapp:{to_number}"
            message = self.client.messages.create(
                body=body,
                from_=self.from_number,
                to=to
            )
            logger.info("Message sent: %s", message.sid)
            return True, getattr(message, "sid", None)
        except Exception as e:
            # Catch Twilio errors, network errors, etc.
            logger.exception("Error sending WhatsApp message")
            return False, str(e)
