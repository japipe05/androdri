from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import contact_route
from app.utils.exceptions import EmailSendError, InvalidContactError
from app.config.settings import settings  # 👈 importar


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
    )

    # 🔹 Middleware CORS (desde .env)
    if settings.ALLOWED_ORIGINS.strip() == "*":
        allowed_origins = ["*"]  # permite todos los orígenes
    else:
        allowed_origins = [origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 🔹 Rutas
    app.include_router(contact_route.router)

    # 🔹 Handlers de errores personalizados
    @app.exception_handler(EmailSendError)
    async def email_send_error_handler(request: Request, exc: EmailSendError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status": "error", "message": exc.detail},
        )

    @app.exception_handler(InvalidContactError)
    async def invalid_contact_handler(request: Request, exc: InvalidContactError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status": "error", "message": exc.detail},
        )

    return app


app = create_app()
