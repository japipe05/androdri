import pytest

from app.domain.entities import Email
from app.domain.exceptions import (
    EmailDeliveryError,
    InvalidEmailError,
    RateLimitExceededError,
    SenderNotAllowedError,
)


def make_email(**kw) -> Email:
    data = dict(
        receptor="a@b.com", emisor="no-reply@Androdri.com", asunto="Hola", mensaje="Mensaje"
    )
    return Email(**{**data, **kw})


async def test_sends_email(use_case, sender):
    result = await use_case.execute(make_email(), "ip-1")
    assert result.message_id == "<fake-id@test>"
    assert result.remaining_emails == 2
    assert len(sender.sent) == 1


async def test_fourth_email_is_blocked(use_case):
    for _ in range(3):
        await use_case.execute(make_email(), "ip-1")
    with pytest.raises(RateLimitExceededError) as exc:
        await use_case.execute(make_email(), "ip-1")
    assert exc.value.retry_after_seconds > 0


async def test_sender_domain_not_allowed(use_case):
    with pytest.raises(SenderNotAllowedError):
        await use_case.execute(make_email(emisor="x@evil.com"), "ip-1")


async def test_failed_delivery_does_not_consume_quota(use_case, sender):
    sender.error = EmailDeliveryError()
    for _ in range(5):
        with pytest.raises(EmailDeliveryError):
            await use_case.execute(make_email(), "ip-1")

    sender.error = None
    result = await use_case.execute(make_email(), "ip-1")
    assert result.remaining_emails == 2


def test_header_injection_is_rejected():
    with pytest.raises(InvalidEmailError):
        make_email(asunto="Hola\r\nBcc: victima@x.com")
