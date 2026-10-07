import logging

from app.container import Container, build_container
from app.infrastructure.config.settings import Settings


def test_build_container_returns_container(settings):
    container = build_container(settings)

    assert isinstance(container, Container)
    assert container.send_email is not None


def test_build_container_warns_when_smtp_username_is_empty(
    settings,
    caplog,
):
    settings.smtp_username = ""

    with caplog.at_level(logging.WARNING):
        container = build_container(settings)

    assert container.send_email is not None
    assert "Credenciales SMTP vacías" in caplog.text


def test_build_container_warns_when_smtp_password_is_empty(
    settings,
    caplog,
):
    from pydantic import SecretStr

    settings.smtp_password = SecretStr("")

    with caplog.at_level(logging.WARNING):
        container = build_container(settings)

    assert container.send_email is not None
    assert "Credenciales SMTP vacías" in caplog.text