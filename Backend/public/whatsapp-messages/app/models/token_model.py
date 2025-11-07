"""
===============================================================================
Archivo:        settings.py
Ubicación:      app/models/token_model.py
Descripción:    Define los modelos Pydantic para el manejo de autenticación
                basada en tokens JWT dentro de la aplicación FastAPI.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0001af
===============================================================================
"""
from pydantic import BaseModel

class TokenRequest(BaseModel):
    api_key: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"