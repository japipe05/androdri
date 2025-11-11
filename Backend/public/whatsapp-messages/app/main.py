"""
===============================================================================
Archivo:        main.py
Ubicación:      app/main.py
Descripción:    Punto de entrada principal de la aplicación FastAPI. Configura
                la instancia principal de la API, define la política de CORS,
                incluye los routers de cada módulo y establece un manejador 
                global de excepciones.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0007af
===============================================================================
"""

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config.settings import settings
from app.routers import meta_router, token_router, whatsapp_router


# ------------------------------------------------------------------------------
# Inicialización de la aplicación FastAPI
# ------------------------------------------------------------------------------
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
# Configuración CORS (Cross-Origin Resource Sharing)
# ------------------------------------------------------------------------------
# Permite que clientes web externos (por ejemplo, frontends) puedan acceder a la API.
# Los orígenes permitidos se definen en settings.ALLOWED_ORIGINS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(u) for u in settings.ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------------------------------------
# Inclusión de Routers
# ------------------------------------------------------------------------------
# Cada router gestiona un conjunto de endpoints independientes.
# - meta_router: información general y documentación
# - token_router: emisión de tokens JWT (autenticación)
# - whatsapp_router: envío de mensajes WhatsApp (servicio principal)
app.include_router(meta_router.router)
app.include_router(token_router.router)
app.include_router(whatsapp_router.router)


# ------------------------------------------------------------------------------
# Manejador global de excepciones
# ------------------------------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Maneja de forma global las excepciones no capturadas en la aplicación.

    ### Descripción
    Intercepta cualquier error inesperado que ocurra durante la ejecución de 
    una solicitud y devuelve una respuesta genérica segura al cliente, evitando
    filtrar detalles internos del sistema.

    ### Parámetros
    - **request** (`Request`): Objeto de solicitud que causó el error.
    - **exc** (`Exception`): Excepción capturada.

    ### Retorna
    - `JSONResponse` con código **500 Internal Server Error** y mensaje genérico.

    ### Ejemplo de respuesta
    ```json
    {
        "detail": "Internal server error"
    }
    ```

    ### Nota
    En un entorno productivo, se recomienda registrar el error en un sistema
    de monitoreo (como Sentry, Logstash o Prometheus).
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )
