# tests/test_whatsapp_api.py
from fastapi.testclient import TestClient
from app.main import app
from app.utils.jwt_utils import create_token

client = TestClient(app)

def test_send_whatsapp_message(monkeypatch):
    # Simular envío Twilio
    def mock_send_message(phone_number, message):
        return {"sid": "fake_sid_123", "status": "sent"}

    # Patch temporal del servicio real
    monkeypatch.setattr("app.services.whatsapp_service.send_whatsapp_message", mock_send_message)

    # Crear JWT válido
    token = create_token({"user": "tester"})

    payload = {
        "phone_number": "+573224613382",
        "message": "Mensaje de prueba desde Pytest 🚀"
    }

    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/api/whatsapp/v1", json=payload, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert data["success"] is True
    assert data["response"]["status"] == "sent"
