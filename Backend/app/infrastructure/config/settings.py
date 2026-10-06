from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # App meta
    environment: str = ""
    app_name: str = ""
    app_version: str = ""
    app_description: str = ""
    app_fechamod: str = ""

    # CORS (lista separada por comas)
    allowed_origins: str = ""

    # Amazon SES SMTP
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_username: str = ""
    smtp_password: SecretStr = SecretStr("")
    smtp_timeout_seconds: int = 10

    # Seguridad
    api_key: SecretStr | None = None
    allowed_sender_domains: str = ""

    # Rate limit
    rate_limit_max_emails: int = 3
    rate_limit_window_seconds: int = 3600

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"

    @property
    def allowed_origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]

    @property
    def allowed_sender_domains_set(self) -> frozenset[str]:
        return frozenset(
            d.strip().lower() for d in self.allowed_sender_domains.split(",") if d.strip()
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
