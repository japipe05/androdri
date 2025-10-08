from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_obtener_token_y_enviar_correo(tmp_path):
    # 1️⃣ Obtener token desde /api/token/
    token_response = client.get("/api/token/")
    assert token_response.status_code == 200

    token_data = token_response.json()
    assert "token" in token_data
    token = token_data["token"]

    # 2️⃣ Crear un archivo temporal simulado
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Archivo de prueba para envío de correo")

    # 3️⃣ Enviar correo usando token
    files = {"archivos": ("test.txt", open(temp_file, "rb"), "text/plain")}
    data = {
        "asunto": "Prueba desde test automático",
        "mensaje": "Este es un correo de prueba generado por Pytest",
        "comprimir": "true",
        "password": "12345"
    }

    response = client.post(
        "/api/contact/v1/",
        headers={"Authorization": f"Bearer {token}"},
        data=data,
        files=files
    )

    # 4️⃣ Verificar resultado
    assert response.status_code == 200
    json_resp = response.json()
    assert "message" in json_resp
    assert "Correo enviado exitosamente" in json_resp["message"]
