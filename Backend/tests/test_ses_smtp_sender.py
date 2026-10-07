import smtplib

import pytest

from app.domain.entities import Email
from app.domain.exceptions import EmailDeliveryError, EmailRejectedError
from app.infrastructure.email.html_renderer import HtmlEmailRenderer
from app.infrastructure.email.ses_smtp_sender import SesSmtpEmailSender


class FakeSMTP:
    instance: "FakeSMTP | None" = None
    error: Exception | None = None

    def __init__(self, host, port, timeout=None):
        self.host, self.port, self.timeout = host, port, timeout
        self.calls: list = []
        self.sent = None
        FakeSMTP.instance = self

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def ehlo(self):
        self.calls.append("ehlo")

    def starttls(self, context=None):
        self.calls.append("starttls")

    def login(self, user, password):
        self.calls.append(("login", user))

    def send_message(self, message):
        if FakeSMTP.error:
            raise FakeSMTP.error
        self.calls.append("send")
        self.sent = message


@pytest.fixture(autouse=True)
def fake_smtp(monkeypatch):
    FakeSMTP.error = None
    monkeypatch.setattr(smtplib, "SMTP", FakeSMTP)


def build():
    email = Email("dest@example.com", "no-reply@Androdri.com", "Hola 🎉", "Mensaje 💬")
    rendered = HtmlEmailRenderer("Androdri").render(email)
    sender = SesSmtpEmailSender("smtp.test", 587, "user", "pass")
    return sender, email, rendered


async def test_uses_starttls_login_and_sends_html():
    sender, email, rendered = build()
    message_id = await sender.send(email, rendered)

    smtp = FakeSMTP.instance
    assert smtp.port == 587
    assert smtp.calls.index("starttls") < smtp.calls.index(("login", "user")) < smtp.calls.index("send")
    assert smtp.sent["Subject"].startswith("📧")
    assert "💬" in smtp.sent.get_body(preferencelist=("html",)).get_content()
    assert message_id == smtp.sent["Message-ID"]


async def test_maps_refused_sender_to_rejected():
    FakeSMTP.error = smtplib.SMTPSenderRefused(554, b"not verified", "x@y.com")
    sender, email, rendered = build()
    with pytest.raises(EmailRejectedError):
        await sender.send(email, rendered)


async def test_maps_smtp_and_network_errors_to_delivery_error():
    sender, email, rendered = build()
    for error in (smtplib.SMTPAuthenticationError(535, b"bad creds"), TimeoutError()):
        FakeSMTP.error = error
        with pytest.raises(EmailDeliveryError):
            await sender.send(email, rendered)
