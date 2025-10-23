# app/config/settings.py
from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Androdri"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Backend para la aplicación Androdri"

    JWT_SECRET_WHATSAP: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES_SECONDS: int = 3600

    TWILIO_ACCOUNT_SID: str | None = None
    TWILIO_AUTH_TOKEN: str | None = None
    TWILIO_WHATSAPP_NUMBER: str | None = None

    RATE_LIMIT_MAX: int = 10
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    ALLOWED_ORIGINS: List[AnyHttpUrl] = [
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "https://api.androdri.com",
    ]

    # Indica dónde está tu .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# instancia única de settings que puedes importar en la app
settings = Settings()
