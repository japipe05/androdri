from twilio.rest import Client
from app.config.settings import settings

class WhatsAppService:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.sender = f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}"

    def send_message(self, to: str, message: str) -> dict:
        try:
            to_whatsapp = f"whatsapp:{to}"
            msg = self.client.messages.create(
                body=message,
                from_=self.sender,
                to=to_whatsapp
            )
            return {"status": "success", "sid": msg.sid}
        except Exception as e:
            return {"status": "error", "detail": str(e)}
