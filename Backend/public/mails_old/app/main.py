"""
===============================================================================
Archivo:        main.py
Ubicación:      app/main.py
Descripción:    Punto de entrada principal de la aplicación FastAPI. Configura
                el objeto principal `app`, inicializa los middlewares globales
                (como CORS), define el esquema de seguridad y registra los
                routers correspondientes a los distintos módulos del sistema.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0011af
===============================================================================
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.config.settings import settings
from app.routers import meta_router, token_router, email_router


# ------------------------------------------------------------------------------
# Inicialización de seguridad y aplicación
# ------------------------------------------------------------------------------
security = HTTPBearer()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    contact={
        "name": "Andres Felipe Rodriguez Roa",
        "url": "https://github.com/japipe05",
        "email": "felipehuchija@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
)


# ------------------------------------------------------------------------------
# Configuración de CORS
# ------------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------------------------------------
# Inclusión de Routers
# ------------------------------------------------------------------------------
app.include_router(meta_router.router)
app.include_router(token_router.router)
app.include_router(email_router.router)


# ------------------------------------------------------------------------------
# Evento de arranque opcional
# ------------------------------------------------------------------------------
@app.on_event("startup")
async def startup_event():
    """
    Evento que se ejecuta al iniciar la aplicación.
    Puede usarse para inicializar conexiones, cachés o tareas de monitoreo.
    """
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} iniciado correctamente.")


