"""Puertos (interfaces) que el núcleo necesita. Los adaptadores los implementan."""

from dataclasses import dataclass
from typing import Protocol

from app.domain.entities import Email, RenderedEmail


@dataclass(frozen=True, slots=True)
class RateLimitDecision:
    allowed: bool
    remaining: int
    retry_after_seconds: int


class EmailSenderPort(Protocol):
    async def send(self, email: Email, rendered: RenderedEmail) -> str:
        """Envía el correo y devuelve el Message-ID."""


class EmailRendererPort(Protocol):
    def render(self, email: Email) -> RenderedEmail: ...


class RateLimiterPort(Protocol):
    async def acquire(self, key: str) -> RateLimitDecision:
        """Intenta consumir un cupo para `key`."""

    async def release(self, key: str) -> None:
        """Devuelve el último cupo consumido (si el envío falló)."""
