import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_send_whatsapp_success():
    """
    Prueba que el endpoint /api/whatsapp/v1 envíe un mensaje correctamente.
    """
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        payload = {
            "phone_number": "+573224612382",  # Usa un número verificado en Twilio
            "message": "Hola desde FastAPI WhatsApp AMBIENTE TEST! 🚀"
        }
        response = await ac.post("/api/whatsapp/v1/", json=payload)

        # Verifica respuesta
        assert response.status_code == 200
        data = response.json()
        assert "sid" in data
        assert data["message"] == "Message sent successfully"

@pytest.mark.asyncio
async def test_send_whatsapp_invalid_number():
    """
    Prueba que el endpoint devuelva 400 cuando se envía un número inválido.
    """
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        payload = {
            "phone_number": "9999",  # Formato incorrecto
            "message": "Esto debe fallar"
        }
        response = await ac.post("/api/whatsapp/v1/", json=payload)

        # Verifica error
        assert response.status_code == 400
        assert "detail" in response.json()

import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_send_whatsapp_twilio_error(monkeypatch):
    """
    Simula un error de Twilio para cubrir la rama de excepción.
    """

    # Clase falsa que imita el cliente Twilio
    class MockMessages:
        def create(self, *args, **kwargs):
            raise Exception("Simulated Twilio error")

    class MockClient:
        def __init__(self, *args, **kwargs):
            self.messages = MockMessages()

    # Reemplaza el cliente Twilio original con el mock
    import app.services.whatsapp_service as ws
    monkeypatch.setattr(ws, "Client", MockClient)

    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        payload = {
            "phone_number": "+573000000000",
            "message": "Esto debe fallar por mock"
        }
        response = await ac.post("/api/whatsapp/v1/", json=payload)

        # Verifica la respuesta
        assert response.status_code == 400
        assert "detail" in response.json()
