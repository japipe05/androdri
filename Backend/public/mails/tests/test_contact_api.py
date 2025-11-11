"""
===============================================================================
Archivo:        test_contact_api.py
Ubicación:      tests/test_contact_api.py
Descripción:    Pruebas automatizadas para la API de contacto por correo.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0007af
===============================================================================
"""

from fastapi.testclient import TestClient
from app.main import app
from app.config.settings import settings
import pytest

client = TestClient(app)



def test_meta_root_info():
    """
    Verifica que el endpoint raíz de meta devuelva información general de la API.
    """
    response = client.get("/")
    assert response.status_code == 200, f"Error en /api/meta/: {response.text}"

    data = response.json()
    assert "app" in data
    assert "version" in data
    assert "description" in data
    assert "docs" in data
    assert "Swagger UI" in data["docs"]
    assert data["app"] == settings.APP_NAME

    print(f"✅ Información de la API obtenida correctamente: {data['app']} v{data['version']}")


# ---------------------------------------------------------------------------
# 1️⃣ Obtener Token JWT
# ---------------------------------------------------------------------------
def test_generate_token():
    payload = {"api_key": settings.JWT_SECRET_KEY}
    response = client.post("/api/token-email/v1/", json=payload)
    assert response.status_code == 200, f"Error al generar token: {response.text}"

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    print(f"✅ Token generado: {data['access_token'][:40]}...")
    return data["access_token"]


# ---------------------------------------------------------------------------
# 2️⃣ Enviar Correo
# ---------------------------------------------------------------------------
@pytest.mark.dependency(depends=["test_generate_token"])
def test_send_email(tmp_path):
    token_payload = {"api_key": settings.JWT_SECRET_KEY}
    token_response = client.post("/api/token-email/v1/", json=token_payload)
    token = token_response.json()["access_token"]

    # Crear archivo de prueba
    temp_file = tmp_path / "archivo_prueba.txt"
    temp_file.write_text("Contenido de prueba generado por Pytest.")

    files = {"archivos": ("archivo_prueba.txt", open(temp_file, "rb"), "text/plain")}
    data = {
        "asunto": "Prueba automática 📧",
        "mensaje": "Correo enviado desde test automatizado",
        "comprimir": "true",
        "password": "12345"
    }

    response = client.post(
        "/api/email/v1/",
        headers={"Authorization": f"Bearer {token}"},
        data=data,
        files=files
    )

    assert response.status_code == 200, f"Error: {response.text}"
    result = response.json()
    assert "message" in result
    assert "Correo enviado" in result["message"]
    print("✅ Envío de correo exitoso.")


# ---------------------------------------------------------------------------
# 3️⃣ Token inválido
# ---------------------------------------------------------------------------
def test_send_email_invalid_token(tmp_path):
    temp_file = tmp_path / "invalido.txt"
    temp_file.write_text("Archivo inválido.")
    files = {"archivos": ("invalido.txt", open(temp_file, "rb"), "text/plain")}
    data = {
        "asunto": "Token inválido",
        "mensaje": "Prueba con token erróneo"
    }

    response = client.post(
        "/api/email/v1/",
        headers={"Authorization": "Bearer token_invalido"},
        data=data,
        files=files
    )

    assert response.status_code == 401
    assert "detail" in response.json()
    print("✅ Token inválido correctamente rechazado.")
