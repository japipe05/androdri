import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

API_KEY = os.getenv("JWT_SECRET_WHATSAP", "your_jwt_secret_here")
PHONE_TO = os.getenv("TEST_PHONE_TO", "+573224612382")


@pytest.fixture(scope="session")
def token():
    """Genera dinámicamente un JWT usando el endpoint /api/token-whatsapp/v1/"""
    response = client.post("/api/token-whatsapp/v1/", json={"api_key": API_KEY})
    assert response.status_code == 200, f"Error generando token: {response.text}"
    data = response.json()
    return data["access_token"]


def test_send_whatsapp_real_twilio(token):
    """
    Envía un mensaje real a WhatsApp usando Twilio y verifica que la API responde correctamente.
    Requiere variables de entorno TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER.
    """
    payload = {
        "phone_number": PHONE_TO,
         "message": (
        "💙*Test Androdri API – Notificación automática*\n\n"
        "📘Se ha realizado una prueba exitosa de conexión con WhatsApp Business.\n"
        "🕒_Fecha:_ 2025-11-06\n"
        "🔹 Estado: Envío confirmado"
    )
    }

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/whatsapp/v1/", json=payload, headers=headers)

    assert response.status_code == 200, f"Error HTTP: {response.text}"

    data = response.json()
    assert data["ok"] is True, f"Respuesta inesperada: {data}"
    result = data["result"]

    # Validaciones comunes en Twilio
    assert "sid" in result, "Falta el SID de Twilio"
    assert result["status"] in ("queued", "sent", "delivered"), f"Estado inesperado: {result['status']}"

    print(f"✅ Mensaje Twilio SID: {result['sid']} | Estado: {result['status']}")


def test_root_endpoint():
    """Verifica que el endpoint raíz devuelva la versión de la API."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )



from app.services.whatsapp_service import WhatsAppService
from fastapi import HTTPException

def test_whatsapp_service_invalid_phone():
    """Debe fallar si el número no inicia con '+'"""
    service = WhatsAppService()
    with pytest.raises(HTTPException) as e:
        service.send_message("12345", "Mensaje")
    assert e.value.status_code == 400
    assert "phone_number" in e.value.detail


def test_whatsapp_service_simulated_send(monkeypatch):
    """Simula envío sin Twilio (modo local)"""
    service = WhatsAppService()
    service.client = None
    result = service.send_message("+573001234567", "Mensaje de prueba")
    assert result["status"] == "sent"
    assert result["to"].startswith("+57")

from app.utils import jwt_utils
from datetime import datetime, timedelta
import jwt

def test_verify_token_valid():
    """Token válido"""
    payload = {"sub": "test", "exp": datetime.utcnow() + timedelta(minutes=1)}
    token = jwt.encode(payload, jwt_utils.settings.JWT_SECRET_WHATSAP, algorithm=jwt_utils.settings.JWT_ALGORITHM)
    result = jwt_utils.verify_token(token)
    assert result["sub"] == "test"

def test_verify_token_invalid():
    """Token inválido"""
    with pytest.raises(Exception):
        jwt_utils.verify_token("invalid.token")

def test_verify_token_expired():
    """Token expirado"""
    payload = {"sub": "test", "exp": datetime.utcnow() - timedelta(minutes=1)}
    token = jwt.encode(payload, jwt_utils.settings.JWT_SECRET_WHATSAP, algorithm=jwt_utils.settings.JWT_ALGORITHM)
    with pytest.raises(Exception):
        jwt_utils.verify_token(token)
