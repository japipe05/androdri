import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr

from app.application.send_email import SendEmailUseCase
from app.container import Container
from app.domain.entities import Email, RenderedEmail
from app.infrastructure.config.settings import Settings
from app.infrastructure.email.html_renderer import HtmlEmailRenderer
from app.infrastructure.rate_limit.memory_limiter import InMemorySlidingWindowRateLimiter
from app.main import create_app

API_KEY = "test-api-key"


class FakeSender:
    def __init__(self) -> None:
        self.sent: list[tuple[Email, RenderedEmail]] = []
        self.error: Exception | None = None

    async def send(self, email: Email, rendered: RenderedEmail) -> str:
        if self.error:
            raise self.error
        self.sent.append((email, rendered))
        return "<fake-id@test>"


class FakeClock:
    def __init__(self) -> None:
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


@pytest.fixture
def sender() -> FakeSender:
    return FakeSender()


@pytest.fixture
def clock() -> FakeClock:
    return FakeClock()


@pytest.fixture
def settings() -> Settings:
    return Settings(
        _env_file=None,

        # App
        environment="testing",
        app_name="FastAPI Androdri",
        app_version="1.0.0",
        app_description="Backend para la aplicación Androdri",
        app_fechamod="2026/10/05 9:35:01",

        # CORS
        allowed_origins="http://localhost:3000",

        # SMTP - valores ficticios para tests
        smtp_host="localhost",
        smtp_port=587,
        smtp_username="test",
        smtp_password=SecretStr("test"),
        smtp_timeout_seconds=10,

        # Seguridad
        api_key=SecretStr(API_KEY),
        allowed_sender_domains="Androdri.com",

        # Rate limit
        rate_limit_max_emails=3,
        rate_limit_window_seconds=3600,
    )


@pytest.fixture
def limiter(clock) -> InMemorySlidingWindowRateLimiter:
    return InMemorySlidingWindowRateLimiter(3, 3600, clock=clock)


@pytest.fixture
def use_case(sender, limiter, settings) -> SendEmailUseCase:
    return SendEmailUseCase(
        sender=sender,
        renderer=HtmlEmailRenderer("Androdri"),
        rate_limiter=limiter,
        allowed_sender_domains=settings.allowed_sender_domains_set,
    )


@pytest.fixture
def client(settings, use_case) -> TestClient:
    return TestClient(create_app(settings, Container(send_email=use_case)))


@pytest.fixture
def auth() -> dict[str, str]:
    return {"X-API-Key": API_KEY}


@pytest.fixture
def payload() -> dict[str, str]:
    return {
        "receptor": "cliente@example.com",
        "emisor": "no-reply@Androdri.com",
        "asunto": "Bienvenido 🎉",
        "mensaje": "Hola 👋\nGracias por registrarte 🙌",
    }
