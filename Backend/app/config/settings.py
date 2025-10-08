from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Androdri"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Backend para la aplicación Androdri"
    ALLOWED_ORIGINS: List[str] = [
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "https://api.androdri.com"
    ]

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str

    JWT_SECRET_KEY: str
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
