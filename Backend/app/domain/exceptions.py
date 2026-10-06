"""Excepciones de dominio. No dependen de FastAPI ni de ninguna librería externa."""


class DomainError(Exception):
    code = "domain_error"
    message = "Error de dominio."

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.message
        super().__init__(self.message)


class InvalidEmailError(DomainError):
    code = "invalid_email"
    message = "Los datos del correo no son válidos."


class SenderNotAllowedError(DomainError):
    code = "sender_not_allowed"
    message = "El dominio del emisor no está autorizado."


class RateLimitExceededError(DomainError):
    code = "rate_limit_exceeded"
    message = "Límite de envíos alcanzado. Intenta de nuevo más tarde."

    def __init__(self, retry_after_seconds: int) -> None:
        self.retry_after_seconds = retry_after_seconds
        minutes = max(1, -(-retry_after_seconds // 60))
        super().__init__(
            f"Límite de envíos alcanzado. Podrás volver a enviar en ~{minutes} min."
        )


class EmailRejectedError(DomainError):
    code = "email_rejected"
    message = "El proveedor rechazó el emisor o el receptor."


class EmailDeliveryError(DomainError):
    code = "email_delivery_failed"
    message = "No se pudo entregar el correo al proveedor. Intenta más tarde."
