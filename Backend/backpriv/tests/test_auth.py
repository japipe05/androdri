from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register():

    response = client.post(
        "/auth/register",
        params={
            "username": "test",
            "email": "test@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200


def test_login():

    response = client.post(
        "/auth/login",
        params={
            "username": "test",
            "password": "123456"
        }
    )

    assert response.status_code == 200