import secrets

from fastapi import Header, HTTPException, Request, status

from app.application.send_email import SendEmailUseCase


def get_send_email_use_case(request: Request) -> SendEmailUseCase:
    return request.app.state.container.send_email


def get_client_key(request: Request) -> str:
    """Clave del rate limit: IP del cliente (usa uvicorn --proxy-headers detrás de un proxy)."""
    return request.client.host if request.client else "unknown"


async def verify_api_key(request: Request, x_api_key: str | None = Header(default=None)) -> None:
    api_key = request.app.state.settings.api_key
    expected = api_key.get_secret_value() if api_key is not None else ""
    if not expected:  # API key deshabilitada
        return
    provided = x_api_key or ""
    if not secrets.compare_digest(provided.encode(), expected.encode()):  # tiempo constante
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="API key inválida o ausente.")
