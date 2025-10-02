import os
import json
from pydantic import BaseSettings, AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Androdri"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Backend para Androdri"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://127.0.0.1:8000", "http://localhost:3000"]

    # SMTP
    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USER: str
    SMTP_PASSWORD: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60

    # Admin simple
    ADMIN_USER: str = "admin"
    ADMIN_PASS: str = "admin"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @classmethod
    def from_env(cls):
        # handle ALLOWED_ORIGINS as json list if provided as string
        raw = cls()
        if isinstance(raw.ALLOWED_ORIGINS, str):
            try:
                raw.ALLOWED_ORIGINS = json.loads(raw.ALLOWED_ORIGINS)
            except Exception:
                raw.ALLOWED_ORIGINS = [raw.ALLOWED_ORIGINS]
        return raw

settings = Settings.from_env()
