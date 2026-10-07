from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class SendEmailRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    receptor: EmailStr = Field(default="feliperodriguez96@hotmail.com",description="Correo del destinatario")
    emisor: EmailStr = Field(default="felipehuchija@gmail.com",description="Correo remitente (verificado en SES)")
    asunto: str = Field(default="Asunto descripcion",min_length=1, max_length=150, description="Asunto (se añade emoji 📧)")
    mensaje: str = Field(default="Solicito mas infromacion sobre la pagina web y una sesion",min_length=1, max_length=5000, description="Mensaje; admite emojis 😀")

    @field_validator("asunto")
    @classmethod
    def no_line_breaks(cls, value: str) -> str:
        if "\r" in value or "\n" in value:
            raise ValueError("El asunto no puede contener saltos de línea")
        return value


class SendEmailResponse(BaseModel):
    success: bool = True
    message: str = "✅ Correo enviado correctamente"
    message_id: str
    remaining_emails: int


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: list[dict] | None = None


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail
