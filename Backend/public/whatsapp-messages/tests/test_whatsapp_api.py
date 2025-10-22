# tests/test_whatsapp_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import create_app
from app.utils.jwt_utils import create_access_token

app = create_app()
client = TestClient(app)

@pytest.fixture
def token():
    return create_access_token("test-user")

def test_send_message_unauthorized():
    resp = client.post("/api/whatsapp/send", json={"phone_number": "+5215512345678", "message": "hola"})
    assert resp.status_code == 401

def test_send_message_bad_phone(token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/api/whatsapp/send", headers=headers, json={"phone_number": "5551234", "message": "hola"})
    assert resp.status_code == 422

# The following test will attempt to call Twilio — in CI you may want to mock the Twilio Client.
# For demonstration we skip live sending.
