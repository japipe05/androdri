from fastapi import FastAPI
from app.routers import whatsapp_router

app = FastAPI(title="WhatsApp Messaging API")

app.include_router(whatsapp_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to the WhatsApp API 🚀"}
