from fastapi import FastAPI
from app.core.config import settings

from app.api import auth_router
from app.api import pagos_router
from app.api import actividades_router
from app.api import meta_router   # 👈 corregido

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
 
app.include_router(meta_router.router)
app.include_router(auth_router.router)
app.include_router(pagos_router.router)
app.include_router(actividades_router.router)