# tests/test_whatsapp_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Este valor debe coincidir con JWT_SECRET_WHATSAP de tu .env
API_KEY = "your_jwt_secret_here"

@pytest.fixture
def token():
    """Genera dinámicamente un JWT usando /api/token-whatsapp/v1/"""
    response = client.post("/api/token-whatsapp/v1/", json={"api_key": API_KEY})
    assert response.status_code == 200
    data = response.json()
    return data["access_token"]

def test_send_whatsapp_with_generated_token(token, monkeypatch):
    """Envía mensaje usando token dinámico"""
    
    # Mock del servicio para no depender de Twilio real
    class MockService:
        @staticmethod
        def send_message(to: str, body: str):
            return {"to": to, "body": body, "status": "mocked"}

    monkeypatch.setattr("app.routers.whatsapp_router.whatsapp_service", MockService)

    payload = {
        "phone_number": "+573001234567",
        "message": "Hola desde Androdri API"
    }

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/whatsapp/v1/send", json=payload, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True
    assert data["result"]["to"] == payload["phone_number"]
    assert data["result"]["body"] == payload["message"]

def test_send_whatsapp_missing_token():
    """Debe fallar si no se envía token"""
    payload = {
        "phone_number": "+573224612382",
        "message": "Hola desde Androdri API"
    }
    response = client.post("/api/whatsapp/v1/send", json=payload)
    assert response.status_code in (401, 403)  # 403 si Depends devuelve Forbidden
    assert "detail" in response.json()
