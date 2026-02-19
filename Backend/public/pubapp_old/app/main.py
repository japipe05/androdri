from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
app = FastAPI(title="Mail Service")

@app.get("/")
async def root():
    base_url = "".rstrip("/")
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

@app.get("/health")
async def health():
    return {"status": "healthy"}

app.include_router(api_router, prefix="/api/v1")
