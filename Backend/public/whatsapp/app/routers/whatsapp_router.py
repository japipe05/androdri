from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.whatsapp_service import WhatsAppService

router = APIRouter(prefix="/api/whatsapp/v1", tags=["WhatsApp"])

class WhatsAppMessage(BaseModel):
    phone_number: str
    message: str

@router.post("/")
def send_whatsapp_message(payload: WhatsAppMessage):
    service = WhatsAppService()
    response = service.send_message(payload.phone_number, payload.message)

    if response["status"] == "error":
        raise HTTPException(status_code=400, detail=response["detail"])
    return {"message": "Message sent successfully", "sid": response["sid"]}
