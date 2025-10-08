from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import contact_router, auth_router  # 👈 Importa el nuevo router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router.router)      # 👈 Añádelo primero
app.include_router(contact_router.router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} está en ejecución 🚀",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_description": settings.APP_DESCRIPTION,
        "fecha_modificacion": settings.APP_FECHAMOD,
    }
