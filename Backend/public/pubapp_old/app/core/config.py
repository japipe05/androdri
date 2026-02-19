from pydantic_settings import BaseSettings
from typing import List
class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_FECHAMOD: str

    ALLOWED_ORIGINS: List[str]
    
    SENDGRID_API_KEY: str
    EMAIL_FROM: str
    EMAIL_TO: str

    class Config:
        env_file = ".env"

settings = Settings()



