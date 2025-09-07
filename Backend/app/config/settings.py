from pydantic_settings import BaseSettings
from pydantic import EmailStr, ConfigDict


class Settings(BaseSettings):
    # Server
    PORT: int   
    # SMTP
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: EmailStr
    SMTP_PASSWORD: str
    RECEIVER_EMAIL: EmailStr

    # App metadata
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    # CORS
    ALLOWED_ORIGINS: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUTES: int

    model_config = ConfigDict(env_file=".env")


settings = Settings()
