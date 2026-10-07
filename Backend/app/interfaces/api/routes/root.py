from fastapi import APIRouter, Request


router = APIRouter(tags=["Información"])


@router.get("/", tags=["Información"])
async def root(request: Request):
    base_url = str(request.base_url).rstrip("/")
    settings = request.app.state.settings
    return {"app": settings.app_name,
            "version": settings.app_version,
            "description": settings.app_description,
            "last_modified": settings.app_fechamod,
            "status": 200,
            "docs": {"Swagger UI": f"{base_url}/docs",
                     "ReDoc": f"{base_url}/redoc",
                     "OpenAPI JSON": f"{base_url}/openapi.json",
                     },
            }
