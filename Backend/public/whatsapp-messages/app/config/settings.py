# app/config/settings.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    JWT_SECRET_WHATSAP: str
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_NUMBER: str
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_FECHAMOD: str
    ALLOWED_ORIGINS: List[str]
    RATE_LIMIT_MAX: int = 10
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
