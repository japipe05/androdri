from app.domain.models import EmailRequest
from app.domain.repositories import EmailRepository
from app.core.rate_limiter import InMemoryRateLimiter
from app.infrastructure.template_renderer import TemplateRenderer
from app.core.config import settings


class EmailService:
    def __init__(
        self,
        repository: EmailRepository,
        rate_limiter: InMemoryRateLimiter
    ):
        self.repository = repository
        self.rate_limiter = rate_limiter
        self.template_renderer = TemplateRenderer()

    def process_email(self, request: EmailRequest):
        if not self.rate_limiter.is_allowed(request.correo):
            raise Exception("Rate limit exceeded. Intente nuevamente en 1 hora.")

        subject = f"Nuevo mensaje de {request.nombre}"

        html_content = self.template_renderer.render(
            "email_template.html",
            {
                "nombre": request.nombre,
                "correo": request.correo,
                "mensaje": request.mensaje,
                "receptor": settings.EMAIL_TO,
                "version": settings.APP_VERSION,
            }
        )

        self.repository.send_email(subject, html_content)
