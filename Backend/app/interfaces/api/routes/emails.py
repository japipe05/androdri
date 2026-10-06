from fastapi import APIRouter, Depends

from app.application.send_email import SendEmailUseCase
from app.domain.entities import Email
from app.interfaces.api.dependencies import (
    get_client_key,
    get_send_email_use_case,
    verify_api_key,
)
from app.interfaces.api.schemas import ErrorResponse, SendEmailRequest, SendEmailResponse

router = APIRouter(prefix="/api/v1/emails", tags=["Emails"])


@router.post(
    "/send",
    response_model=SendEmailResponse,
    summary="Enviar un correo HTML con emojis 📧",
    dependencies=[Depends(verify_api_key)],
    responses={
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        429: {"model": ErrorResponse, "description": "Máx. 3 correos por hora"},
        502: {"model": ErrorResponse},
    },
)
async def send_email(
    payload: SendEmailRequest,
    client_key: str = Depends(get_client_key),
    use_case: SendEmailUseCase = Depends(get_send_email_use_case),
) -> SendEmailResponse:
    email = Email(
        receptor=str(payload.receptor),
        emisor=str(payload.emisor),
        asunto=payload.asunto,
        mensaje=payload.mensaje,
    )
    result = await use_case.execute(email, client_key)
    return SendEmailResponse(
        message_id=result.message_id, remaining_emails=result.remaining_emails
    )
