"""
===============================================================================
Archivo:        test_app.py
Ubicación:      tests/test_app.py
Descripción:    Conjunto de pruebas unitarias e integrales para la API WhatsApp
                desarrollada con FastAPI. Valida la correcta emisión de tokens
                JWT, el envío de mensajes (real o simulado), el endpoint raíz y 
                los servicios auxiliares.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/06
Radicado:       v0008af
===============================================================================

Requisitos previos:
-------------------
- Tener configuradas las variables de entorno:
  - JWT_SECRET_WHATSAP
  - TWILIO_ACCOUNT_SID
  - TWILIO_AUTH_TOKEN
  - TWILIO_WHATSAPP_NUMBER
  - TEST_PHONE_TO (teléfono de prueba con prefijo internacional)

Ejecución:
----------
    pytest -v -s tests/test_app.py

Notas:
------
- Si Twilio no está configurado, las pruebas usarán el modo "simulado".
- Las pruebas usan el cliente de TestClient de FastAPI para ejecutar endpoints reales.
===============================================================================
"""

import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

# ------------------------------------------------------------------------------
# Configuración global para las pruebas
# ------------------------------------------------------------------------------
client = TestClient(app)

API_KEY = os.getenv("JWT_SECRET_WHATSAP", "your_jwt_secret_here")
PHONE_TO = os.getenv("TEST_PHONE_TO", "+573224612382")


# ------------------------------------------------------------------------------
# FIXTURE: Generación dinámica del token JWT
# ------------------------------------------------------------------------------
@pytest.fixture(scope="session")
def token():
    """
    Genera dinámicamente un token JWT usando el endpoint 
    `/api/token-whatsapp/v1/`.

    ### Retorna:
    - Cadena de texto con el token JWT válido.
    """
    response = client.post("/api/token-whatsapp/v1/", json={"api_key": API_KEY})
    assert response.status_code == 200, f"Error generando token: {response.text}"
    data = response.json()
    return data["access_token"]


# ------------------------------------------------------------------------------
# TEST: Envío real de mensaje vía Twilio
# ------------------------------------------------------------------------------
def test_send_whatsapp_real_twilio(token):
    """
    Envía un mensaje real a través de Twilio usando la API `/api/whatsapp/v1/`.
    Verifica que la respuesta sea válida y que el mensaje tenga estado 
    correcto.

    Requiere:
    - Variables de entorno `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`,
      y `TWILIO_WHATSAPP_NUMBER`.

    Si las credenciales no están configuradas, la prueba se ejecutará 
    en modo simulado.
    """
    payload = {
        "phone_number": PHONE_TO,
        "message": (
            "💙*Test Androdri API – Notificación automática*\n\n"
            "📘Se ha realizado una prueba exitosa de conexión con WhatsApp Business.\n"
            "🕒_Fecha:_ 2025-11-06\n"
            "🔹 Estado: Envío confirmado"
        ),
    }

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/whatsapp/v1/", json=payload, headers=headers)

    assert response.status_code == 200, f"Error HTTP: {response.text}"

    data = response.json()
    assert data["ok"] is True, f"Respuesta inesperada: {data}"

    result = data["result"]
    assert "sid" in result, "Falta el SID de Twilio"
    assert result["status"] in ("queued", "sent", "delivered", "sent"), f"Estado inesperado: {result['status']}"

    print(f"✅ Mensaje Twilio SID: {result['sid']} | Estado: {result['status']}")


# ------------------------------------------------------------------------------
# TEST: Endpoint raíz de la API
# ------------------------------------------------------------------------------
def test_root_endpoint():
    """Verifica que el endpoint raíz (`/`) devuelva los metadatos de la API."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data


# ------------------------------------------------------------------------------
# TEST: Manejo global de excepciones
# ------------------------------------------------------------------------------
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Simula el manejador global de excepciones definido en `app/main.py`
    para validar el comportamiento de errores inesperados.
    """
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


# ------------------------------------------------------------------------------
# TEST: Servicio WhatsApp (unidad)
# ------------------------------------------------------------------------------
from app.services.whatsapp_service import WhatsAppService
from fastapi import HTTPException

def test_whatsapp_service_invalid_phone():
    """Debe lanzar un error 400 si el número de teléfono no inicia con '+'."""
    service = WhatsAppService()
    with pytest.raises(HTTPException) as e:
        service.send_message("12345", "Mensaje")
    assert e.value.status_code == 400
    assert "phone_number" in e.value.detail


def test_whatsapp_service_simulated_send(monkeypatch):
    """Simula envío sin Twilio (modo local o de pruebas)."""
    service = WhatsAppService()
    service.client = None
    result = service.send_message("+573001234567", "Mensaje de prueba")
    assert result["status"] == "sent"
    assert result["to"].startswith("+57")


# ------------------------------------------------------------------------------
# TEST: Utilidades JWT (creación y verificación de tokens)
# ------------------------------------------------------------------------------
from app.utils import jwt_utils
from datetime import datetime, timedelta
import jwt


def test_verify_token_valid():
    """Debe validar correctamente un token JWT válido."""
    payload = {"sub": "test", "exp": datetime.utcnow() + timedelta(minutes=1)}
    token = jwt.encode(
        payload,
        jwt_utils.settings.JWT_SECRET_WHATSAP,
        algorithm=jwt_utils.settings.JWT_ALGORITHM
    )
    result = jwt_utils.verify_token(token)
    assert result["sub"] == "test"


def test_verify_token_invalid():
    """Debe lanzar excepción si el token es inválido o manipulado."""
    with pytest.raises(Exception):
        jwt_utils.verify_token("invalid.token")


def test_verify_token_expired():
    """Debe lanzar excepción si el token está expirado."""
    payload = {"sub": "test", "exp": datetime.utcnow() - timedelta(minutes=1)}
    token = jwt.encode(
        payload,
        jwt_utils.settings.JWT_SECRET_WHATSAP,
        algorithm=jwt_utils.settings.JWT_ALGORITHM
    )
    with pytest.raises(Exception):
        jwt_utils.verify_token(token)
