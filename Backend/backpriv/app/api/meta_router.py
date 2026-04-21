from fastapi import APIRouter, Request
from app.core.config import settings

router = APIRouter()


@router.get("/", tags=["Meta"], summary="Información general y documentación de la API")
async def root(request: Request):

    base_url = str(request.base_url).rstrip("/")

    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": settings.APP_DESCRIPTION,
        "last_modified": settings.APP_FECHAMOD,
        "docs": {
            "Swagger UI": f"{base_url}/docs",
            "ReDoc": f"{base_url}/redoc",
            "OpenAPI JSON": f"{base_url}/openapi.json"
        },
    }