# app/main.py
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import get_settings
from app.routers.whatsapp_router import router as whatsapp_router

settings = get_settings()

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Routers
    app.include_router(whatsapp_router)

    # ⚙️ Personalizar esquema de seguridad OpenAPI
    @app.on_event("startup")
    async def setup_openapi():
        if app.openapi_schema:
            return
        openapi_schema = app.openapi()
        openapi_schema["components"]["securitySchemes"] = {
            "JWTBearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "Autenticación JWT usando el esquema Bearer. Ejemplo: 'Authorization: Bearer <token>'"
            }
        }
        openapi_schema["security"] = [{"JWTBearerAuth": []}]
        app.openapi_schema = openapi_schema

    # Manejo global de errores
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logging.exception("Unhandled exception")
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
