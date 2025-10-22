# app/models/message_model.py
from pydantic import BaseModel, Field

class WhatsAppMessage(BaseModel):
    phone_number: str = Field(..., example="+573224613382")
    message: str = Field(..., example="Hola desde FastAPI y Twilio 🚀")
