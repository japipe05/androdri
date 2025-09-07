from pydantic import BaseModel, EmailStr, Field


class ContactRequest(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Felipe Huchija"})
    email: EmailStr = Field(..., json_schema_extra={"example": "usuario@gmail.com"})
    message: str = Field(..., json_schema_extra={"example": "Estoy interesado en sus servicios de desarrollo web."})


class ContactResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "success"})
    message: str = Field(..., json_schema_extra={"example": "Mensaje enviado con éxito"})
