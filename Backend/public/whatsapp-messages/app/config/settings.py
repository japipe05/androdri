# app/config/settings.py
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    # App meta
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_FECHAMOD: str

    # JWT
    JWT_SECRET_WHATSAP: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXP_SECONDS: int = 3600

    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_NUMBER: str

    # CORS
    ALLOWED_ORIGINS: List[str] = []

    # Rate limiter
    RATE_LIMIT_MAX: int = 10
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
