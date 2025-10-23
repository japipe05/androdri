
# ------------------------
# File: app/main.py
# ------------------------
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import token_router, whatsapp_router
from fastapi.responses import JSONResponse
from fastapi import status

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, description=settings.APP_DESCRIPTION)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(u) for u in settings.ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(token_router.router)
app.include_router(whatsapp_router.router)

# root
@app.get("/", tags=["root"])
async def root():
    return {"app": settings.APP_NAME, "version": settings.APP_VERSION}

# Global exception handler for validation and unexpected errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Do not leak internal errors; return safe message but log details if needed
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )