from pydantic import BaseModel, EmailStr, Field


class EmailRequest(BaseModel):
    nombre: str = Field(..., min_length=2)
    correo: EmailStr
    mensaje: str = Field(..., min_length=5)


class EmailResponse(BaseModel):
    success: bool
    message: str
