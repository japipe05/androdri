from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_send_email_success():
    response = client.post("/send-email", json={
        "nombre": "Felipe",
        "correo": "felipe@test.com",
        "mensaje": "Hola mundo test"
    })

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_rate_limit():
    for _ in range(5):
        client.post("/send-email", json={
            "nombre": "Felipe",
            "correo": "limit@test.com",
            "mensaje": "Hola mundo"
        })

    response = client.post("/send-email", json={
        "nombre": "Felipe",
        "correo": "limit@test.com",
        "mensaje": "Hola mundo"
    })

    assert response.status_code == 400
