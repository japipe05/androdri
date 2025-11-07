"""
===============================================================================
Archivo:        settings.py
Ubicación:      app/config/settings.py
Descripción:    Configuración central de la aplicación FastAPI. Define y carga
                las variables de entorno utilizando Pydantic Settings para
                asegurar validación y tipado estricto de configuración.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0001af
===============================================================================
"""
from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str 
    APP_FECHAMOD: str

    JWT_SECRET_WHATSAP: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES_SECONDS: int = 3600

    TWILIO_ACCOUNT_SID: str | None = None
    TWILIO_AUTH_TOKEN: str | None = None
    TWILIO_WHATSAPP_NUMBER: str | None = None

    RATE_LIMIT_MAX: int = 10
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    ALLOWED_ORIGINS: List[AnyHttpUrl] 

    # Indica dónde está tu .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# instancia única de settings que puedes importar en la app
settings = Settings()
