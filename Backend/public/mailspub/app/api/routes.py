from fastapi import APIRouter, HTTPException, Depends, Request

from app.domain.models import EmailRequest, EmailResponse
from app.infrastructure.email_service import SendGridEmailService
from app.application.services import EmailService
from app.core.rate_limiter import InMemoryRateLimiter
from app.core.config import settings

router = APIRouter()
rate_limiter = InMemoryRateLimiter()


def get_email_service():
    return EmailService(
        repository=SendGridEmailService(),
        rate_limiter=rate_limiter
    )
    
@router.get("/", tags=["Meta"], summary="Información general y documentación de la API")
async def root(request: Request):
    """
    Devuelve información de la aplicación y enlaces a la documentación interactiva.
    """
    base_url = str(request.base_url).rstrip("/")

    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": settings.APP_DESCRIPTION,
        "last_modified": settings.APP_FECHAMOD,
        "docs": {
            "Swagger UI": f"{base_url}/docs",
            "ReDoc": f"{base_url}/redoc",
            "OpenAPI JSON": f"{base_url}/openapi.json"
        },
    }


@router.post("/send-email", tags=["Mails"],response_model=EmailResponse)
def send_email(
    request: EmailRequest,
    service: EmailService = Depends(get_email_service)
):
    try:
        service.process_email(request)
        return EmailResponse(success=True, message="Email enviado correctamente")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
