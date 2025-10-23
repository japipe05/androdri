
# ------------------------
# File: app/services/whatsapp_service.py
# ------------------------
from app.config.settings import settings
from typing import Dict
from fastapi import HTTPException, status

# Try to use Twilio if credentials are present. Abstract for testing.
try:
    from twilio.rest import Client
except Exception:
    Client = None

class WhatsAppService:
    def __init__(self):
        if Client and settings.TWILIO_ACCOUNT_SID and settings.TWILIO_AUTH_TOKEN:
            self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        else:
            self.client = None

    def send_message(self, to: str, body: str) -> Dict:
        # Validate basic format
        if not to.startswith("+"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="phone_number must start with + and country code")

        # If Twilio client is configured, send real message
        if self.client:
            from_number = f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}"
            to_number = f"whatsapp:{to}"
            try:
                message = self.client.messages.create(body=body, from_=from_number, to=to_number)
                return {"sid": message.sid, "status": message.status}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"provider error: {e}")

        # Fallback: simulate send (useful for local dev/test)
        return {"sid": "SIMULATED-1234", "status": "sent", "to": to, "body": body}

whatsapp_service = WhatsAppService()