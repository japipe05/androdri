from pydantic import BaseModel, Field
from typing import Optional

class EmailRequest(BaseModel):
    asunto: str = Field(..., description="Asunto del correo")
    mensaje: str = Field(..., description="Mensaje del correo")
    comprimir: Optional[bool] = False
    password: Optional[str] = None
