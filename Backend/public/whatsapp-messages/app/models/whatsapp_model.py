"""
===============================================================================
Archivo:        settings.py
Ubicación:      app/models/whatsapp_model.py
Descripción:    Define los modelos de datos utilizados para el envío de mensajes
                de WhatsApp a través de la integración con Twilio o servicios
                similares dentro de la aplicación FastAPI.
Autor:          Andres Felipe Rodriguez Roa
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0001af
===============================================================================
"""
from pydantic import BaseModel, Field

class WhatsAppSendRequest(BaseModel):
    phone_number: str = Field(..., example="+573224612382")
    message: str = Field(..., example="Hola desde Androdri API")
