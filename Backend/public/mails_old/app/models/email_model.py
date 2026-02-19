"""
===============================================================================
Archivo:        email_model.py
Ubicación:      app/models/email_model.py
Descripción:    Define el modelo de datos utilizado para la recepción y validación
                de solicitudes de envío de correo electrónico. Utiliza Pydantic
                para garantizar la integridad, el tipado y la documentación
                automática de los datos a través de FastAPI.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0003af
===============================================================================
"""

from pydantic import BaseModel, Field
from typing import Optional


class EmailRequest(BaseModel):
    """
    Modelo de solicitud para el envío de correos electrónicos.

    Este modelo valida y estructura los datos recibidos por los endpoints
    relacionados con el envío de correos, asegurando que los campos requeridos
    estén correctamente definidos antes de ser procesados por la lógica del
    servicio (por ejemplo, a través de SMTP o un API externo).

    Atributos
    ---------
    asunto : str
        Asunto del correo electrónico.
    mensaje : str
        Cuerpo o contenido principal del correo.
    comprimir : bool, opcional
        Indica si se deben comprimir los archivos adjuntos antes de enviarlos.
        Por defecto, `False`.
    password : Optional[str], opcional
        Contraseña para proteger archivos comprimidos (si aplica). Puede ser `None`.
    """

    asunto: str = Field(..., description="Asunto del correo electrónico.")
    mensaje: str = Field(..., description="Contenido o cuerpo principal del mensaje.")
    comprimir: bool = Field(
        default=False,
        description="Indica si se deben comprimir los archivos adjuntos antes del envío.",
    )
    password: Optional[str] = Field(
        default=None,
        description="Contraseña opcional para proteger los archivos comprimidos.",
    )
