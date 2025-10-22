# app/models/message_model.py
from pydantic import BaseModel, Field
from typing import Optional

class SendMessageRequest(BaseModel):
    phone_number: str = Field(..., example="+5215512345678")
    message: str = Field(..., example="Hola desde FastAPI Androdri!")

class SendMessageResponse(BaseModel):
    success: bool
    sid: Optional[str] = None
    detail: Optional[str] = None
