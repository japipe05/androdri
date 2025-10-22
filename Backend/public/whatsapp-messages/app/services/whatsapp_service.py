# app/services/whatsapp_service.py
from twilio.rest import Client
from app.config.settings import settings

def send_whatsapp_message(phone_number: str, message: str):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            from_=f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}",
            body=message,
            to=f"whatsapp:{phone_number}"
        )
        return {"sid": msg.sid, "status": msg.status}
    except Exception as e:
        raise Exception(f"Error enviando mensaje: {str(e)}")
