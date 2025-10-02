from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers.email_router import router as email_router
from app.routers.auth_router import router as auth_router

app = FastAPI(title=settings.APP_NAME, description=settings.APP_DESCRIPTION, version=settings.APP_VERSION)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(email_router)


@app.get("/")
def root():
    return {"app": settings.APP_NAME, "version": settings.APP_VERSION}
