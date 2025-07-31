from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    RECEIVER_EMAIL: str# 👈 Nuevo campo

    class Config:
        env_file = ".env"

settings = Settings()
