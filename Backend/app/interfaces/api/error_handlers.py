import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.domain.exceptions import (
    DomainError,
    EmailDeliveryError,
    EmailRejectedError,
    InvalidEmailError,
    RateLimitExceededError,
    SenderNotAllowedError,
)

logger = logging.getLogger(__name__)

_STATUS_BY_ERROR: dict[type[DomainError], int] = {
    InvalidEmailError: 422,
    SenderNotAllowedError: 403,
    RateLimitExceededError: 429,
    EmailRejectedError: 422,
    EmailDeliveryError: 502,
}


def _body(code: str, message: str, details: list[dict] | None = None) -> dict:
    error: dict = {"code": code, "message": message}
    if details:
        error["details"] = details
    return {"success": False, "error": error}


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def domain_error_handler(_: Request, exc: DomainError) -> JSONResponse:
        headers = None
        if isinstance(exc, RateLimitExceededError):
            headers = {"Retry-After": str(exc.retry_after_seconds)}
        return JSONResponse(
            status_code=_STATUS_BY_ERROR.get(type(exc), 400),
            content=_body(exc.code, exc.message),
            headers=headers,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
        # Solo campo y mensaje: nunca se devuelve el valor recibido.
        details = [
            {"field": ".".join(str(p) for p in err["loc"][1:]) or "body", "message": err["msg"]}
            for err in exc.errors()
        ]
        return JSONResponse(
            status_code=422,
            content=_body("validation_error", "Datos de entrada inválidos.", details),
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_handler(_: Request, exc: StarletteHTTPException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content=_body("http_error", str(exc.detail)),
            headers=getattr(exc, "headers", None),
        )

    @app.exception_handler(Exception)
    async def unexpected_handler(_: Request, exc: Exception) -> JSONResponse:
        logger.exception("Error no controlado: %s", type(exc).__name__)
        return JSONResponse(
            status_code=500,
            content=_body("internal_error", "Error interno del servidor."),
        )
