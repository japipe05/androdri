"""
===============================================================================
Archivo:        settings.py
Ubicación:      app/routers/meta_router.py
Descripción:    Define las rutas informativas (metadatos) de la API. Proporciona
                detalles generales de la aplicación, incluyendo nombre, versión,
                descripción, fecha de última modificación y enlaces a la 
                documentación interactiva.
Autor:          Andres Felipe Rodriguez Roa
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0001af
===============================================================================
"""
from fastapi import APIRouter, Request
from app.config import settings

router = APIRouter(tags=["Meta"])

@router.get("/", summary="Información general y documentación de la API")
async def root(request: Request):
    """
    Devuelve información de la aplicación y enlaces a la documentación interactiva.
    """
    base_url = str(request.base_url).rstrip("/")

    return {
        "app": settings.settings.APP_NAME,
        "version": settings.settings.APP_VERSION,
        "description": settings.settings.APP_DESCRIPTION,
        "last_modified": settings.settings.APP_FECHAMOD,
        "docs": {
            "Swagger UI": f"{base_url}/docs",
            "ReDoc": f"{base_url}/redoc",
            "OpenAPI JSON": f"{base_url}/openapi.json"
        },
    }
   