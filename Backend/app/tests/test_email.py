import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, MagicMock
import base64

client = TestClient(app)

@pytest.fixture
def token():
    # obtener token con credenciales por defecto del .env (ver settings)
    resp = client.post("/auth/token", json={"username":"admin","password":"admin"})
    assert resp.status_code in (200, 401)  # si no cambias .env puede ser 200
    if resp.status_code == 200:
        return resp.json()["access_token"]
    # si no, fall back: crear un token con endpoint (tests locales deberían configurar ADMIN_USER/PASS)
    pytest.skip("No se pudo obtener token para pruebas. Configure ADMIN_USER/ADMIN_PASS en .env.")

@patch("smtplib.SMTP")
def test_send_email_without_attachments(mock_smtp, token):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "asunto": "Prueba asunto",
        "mensaje": "Este es un cuerpo de prueba",
        "comprimir": "false"
    }
    response = client.post("/email/send", headers=headers, data=data)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    mock_smtp.assert_called_once()

@patch("smtplib.SMTP")
def test_send_email_with_attachments_and_zip(mock_smtp, token):
    headers = {"Authorization": f"Bearer {token}"}
    files = {
        "files": ("archivo.txt", b"Contenido de prueba", "text/plain")
    }
    data = {
        "asunto": "Prueba zip",
        "mensaje": "Cuerpo con zip",
        "comprimir": "true",
        "zip_password": "clave123"
    }
    response = client.post("/email/send", headers=headers, data=data, files=files)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    mock_smtp.assert_called_once()
