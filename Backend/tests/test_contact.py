import pytest
import jwt
from fastapi.testclient import TestClient
from app.main import app
from app.config.settings import settings

client = TestClient(app)

# Fixture que genera un token JWT válido
@pytest.fixture
def jwt_token():
    payload = {"sub": "test_user"}  # payload simulado
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token


def test_contact_missing_field(jwt_token):
    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe Huchija",
            "message": "Falta el email"
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["msg"] == "Field required"


def test_invalid_email(jwt_token):
    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe",
            "email": "no-es-email",
            "message": "Probando error de email"
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )
    assert response.status_code == 422
    data = response.json()
    assert "value is not a valid email address" in data["detail"][0]["msg"]


def test_email_send_error(monkeypatch, jwt_token):
    def mock_send_email(subject, body, sender_email):
        raise Exception("SMTP server not available")

    from app.services import contact_service
    monkeypatch.setattr(contact_service, "send_email", mock_send_email)

    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe",
            "email": "usuario@gmail.com",
            "message": "Prueba fallo SMTP"
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )
    assert response.status_code == 500
    data = response.json()
    assert data["status"] == "error"
    assert "SMTP server not available" in data["message"]


def test_invalid_contact_handler(monkeypatch, jwt_token):
    from app.api.v1 import contact_route
    from app.utils.exceptions import InvalidContactError

    def mock_process_contact(contact):
        raise InvalidContactError("Contacto inválido")

    monkeypatch.setattr(contact_route, "process_contact", mock_process_contact)

    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe",
            "email": "usuario@gmail.com",
            "message": "Mensaje inválido"
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )

    assert response.status_code == 400
    data = response.json()
    assert data["status"] == "error"
    assert "Contacto inválido" in data["message"]


def test_send_contact(monkeypatch, jwt_token):
    """
    Caso exitoso simulado con mock (no envía correo real).
    """
    def mock_send_email(subject, body, sender_email):
        return True

    from app.services import contact_service
    monkeypatch.setattr(contact_service, "send_email", mock_send_email)

    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe Huchija",
            "email": "usuario@gmail.com",
            "message": "Estoy interesado en sus servicios de desarrollo web."
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Mensaje enviado" in data["message"]

@pytest.mark.integration
def test_send_real_email(jwt_token):
    """
    Test de integración que SÍ envía un correo real.
    Se ejecuta solo con: pytest -m integration
    """
    response = client.post(
        "/api/contact/v1/",
        json={
            "name": "Felipe Huchija",
            "email": "usuario@gmail.com",
            "message": "⚡ Test real de envío de correo desde FastAPI ⚡"
        },
        headers={"Authorization": f"Bearer {jwt_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Mensaje enviado" in data["message"]
