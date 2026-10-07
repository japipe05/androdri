from dataclasses import dataclass
import logging

from app.application.ports import EmailRendererPort, EmailSenderPort, RateLimiterPort
from app.domain.entities import Email
from app.domain.exceptions import (
    DomainError,
    RateLimitExceededError,
    SenderNotAllowedError,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class SendEmailResult:
    message_id: str
    remaining_emails: int


class SendEmailUseCase:
    """Caso de uso: valida emisor -> aplica límite -> renderiza -> envía."""

    def __init__(
        self,
        sender: EmailSenderPort,
        renderer: EmailRendererPort,
        rate_limiter: RateLimiterPort,
        allowed_sender_domains: frozenset[str] = frozenset(),
    ) -> None:
        self._sender = sender
        self._renderer = renderer
        self._rate_limiter = rate_limiter
        self._allowed_sender_domains = allowed_sender_domains

    async def execute(self, email: Email, client_key: str) -> SendEmailResult:
        self._ensure_sender_allowed(email)

        decision = await self._rate_limiter.acquire(client_key)
        if not decision.allowed:
            raise RateLimitExceededError(decision.retry_after_seconds)

        try:
            rendered = self._renderer.render(email)
            message_id = await self._sender.send(email, rendered)
        except DomainError:
            # Un envío fallido no debe consumir el cupo del cliente.
            await self._rate_limiter.release(client_key)
            raise
        except Exception:
            await self._rate_limiter.release(client_key)
            raise

        logger.info("Correo enviado message_id=%s", message_id)
        return SendEmailResult(message_id=message_id, remaining_emails=decision.remaining)

    def _ensure_sender_allowed(self, email: Email) -> None:
        if self._allowed_sender_domains and email.emisor_domain not in self._allowed_sender_domains:
            raise SenderNotAllowedError()
