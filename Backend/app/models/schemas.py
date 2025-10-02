from pydantic import BaseModel, Field
from typing import Optional

class EmailSendRequest(BaseModel):
    asunto: str = Field(..., min_length=1, max_length=255, description="Asunto del correo")
    mensaje: str = Field(..., min_length=1, description="Cuerpo del correo")
    comprimir: Optional[bool] = False
    zip_password: Optional[str] = Field(None, min_length=1, max_length=128, description="Clave para el zip (opcional)")

class TokenRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
