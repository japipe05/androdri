from fastapi import APIRouter
from app.api.v1.routes.mail import router as mail_router

api_router = APIRouter()
api_router.include_router(mail_router, prefix="/mail", tags=["Mail"])
