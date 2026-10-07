URL = "/api/v1/emails/send"


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200

    body = response.json()

    # Metadata
    assert body["app"] == "FastAPI Androdri"
    assert body["version"] == "1.0.0"
    assert body["description"] == "Backend para la aplicación Androdri"
    assert body["last_modified"] == "2026/10/05 9:35:01"
    assert body["status"] == 200

    # Documentation endpoints
    docs = body["docs"]

    assert docs["Swagger UI"].endswith("/docs")
    assert docs["ReDoc"].endswith("/redoc")
    assert docs["OpenAPI JSON"].endswith("/openapi.json")

def test_send_ok(client, auth, payload, sender):
    response = client.post(URL, json=payload, headers=auth)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True and body["remaining_emails"] == 2
    assert len(sender.sent) == 1
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_requires_api_key(client, payload):
    response = client.post(URL, json=payload)
    assert response.status_code == 401
    assert response.json()["success"] is False


def test_wrong_api_key(client, payload):
    assert client.post(URL, json=payload, headers={"X-API-Key": "nope"}).status_code == 401


def test_fourth_email_returns_429_with_retry_after(client, auth, payload):
    for _ in range(3):
        assert client.post(URL, json=payload, headers=auth).status_code == 200
    response = client.post(URL, json=payload, headers=auth)
    assert response.status_code == 429
    assert response.json()["error"]["code"] == "rate_limit_exceeded"
    assert 0 < int(response.headers["Retry-After"]) <= 3600


def test_invalid_email_returns_422_without_echoing_input(client, auth, payload):
    payload["receptor"] = "no-es-un-correo"
    response = client.post(URL, json=payload, headers=auth)
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation_error"
    assert "no-es-un-correo" not in response.text


def test_subject_with_line_break_is_rejected(client, auth, payload):
    payload["asunto"] = "Hola\nBcc: x@y.com"
    assert client.post(URL, json=payload, headers=auth).status_code == 422


def test_extra_fields_are_rejected(client, auth, payload):
    payload["bcc"] = "x@y.com"
    assert client.post(URL, json=payload, headers=auth).status_code == 422


def test_sender_domain_not_allowed_returns_403(client, auth, payload):
    payload["emisor"] = "ceo@otro-dominio.com"
    assert client.post(URL, json=payload, headers=auth).status_code == 403


def test_provider_failure_returns_502_without_internal_details(client, auth, payload, sender):
    from app.domain.exceptions import EmailDeliveryError

    sender.error = EmailDeliveryError()
    response = client.post(URL, json=payload, headers=auth)
    assert response.status_code == 502
    assert response.json()["error"]["code"] == "email_delivery_failed"


def test_unexpected_error_returns_500_generic(settings, use_case, sender, auth, payload):
    from fastapi.testclient import TestClient

    from app.container import Container
    from app.main import create_app

    sender.error = RuntimeError("boom con secretos")
    app = create_app(settings, Container(send_email=use_case))
    response = TestClient(app, raise_server_exceptions=False).post(URL, json=payload, headers=auth)
    assert response.status_code == 500
    assert "boom" not in response.text
