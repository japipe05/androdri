import logging

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

from app.container import Container, build_container
from app.infrastructure.config.settings import Settings, get_settings
from app.interfaces.api.error_handlers import register_error_handlers
from app.interfaces.api.routes import emails, root
from app.interfaces.api.security import register_security_headers

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def create_app(settings: Settings | None = None, container: Container | None = None) -> FastAPI:
    """Application factory (permite inyectar settings/fakes en las pruebas)."""
    settings = settings or get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=f"{settings.app_description}\n\nÚltima modificación: {settings.app_fechamod}",
       
    )
    app.state.settings = settings
    app.state.container = container or build_container(settings)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins_list,
        allow_credentials=False,
        allow_methods=["GET", "POST"],
        allow_headers=["Content-Type", "X-API-Key"],
        max_age=600,
    )


    register_security_headers(app, settings.is_production)
    register_error_handlers(app)
    app.include_router(root.router)
    app.include_router(emails.router)
    return app
