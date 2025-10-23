
# ------------------------
# File: app/models/whatsapp_model.py
# ------------------------
from pydantic import BaseModel, Field

class WhatsAppSendRequest(BaseModel):
    phone_number: str = Field(..., example="+573001234567")
    message: str = Field(..., example="Hola desde Androdri API")
