"""Composition root: único lugar donde se ensamblan puertos y adaptadores (DI manual)."""

import logging
from dataclasses import dataclass

from app.application.send_email import SendEmailUseCase
from app.infrastructure.config.settings import Settings
from app.infrastructure.email.html_renderer import HtmlEmailRenderer
from app.infrastructure.email.ses_smtp_sender import SesSmtpEmailSender
from app.infrastructure.rate_limit.memory_limiter import InMemorySlidingWindowRateLimiter

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class Container:
    send_email: SendEmailUseCase


def build_container(settings: Settings) -> Container:
    if not settings.smtp_username or not settings.smtp_password.get_secret_value():
        logger.warning("Credenciales SMTP vacías: el envío fallará hasta configurarlas en .env")
    if settings.is_production and not settings.allowed_sender_domains_set:
        logger.warning("ALLOWED_SENDER_DOMAINS vacío en producción: cualquier emisor es aceptado")

    sender = SesSmtpEmailSender(
        host=settings.smtp_host,
        port=settings.smtp_port,
        username=settings.smtp_username,
        password=settings.smtp_password.get_secret_value(),
        timeout=settings.smtp_timeout_seconds,
    )
    limiter = InMemorySlidingWindowRateLimiter(
        max_requests=settings.rate_limit_max_emails,
        window_seconds=settings.rate_limit_window_seconds,
    )
    return Container(
        send_email=SendEmailUseCase(
            sender=sender,
            renderer=HtmlEmailRenderer(brand_name="Androdri"),
            rate_limiter=limiter,
            allowed_sender_domains=settings.allowed_sender_domains_set,
        )
    )
