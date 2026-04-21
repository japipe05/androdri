from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.domain.repositories import EmailRepository
from app.core.config import settings


class SendGridEmailService(EmailRepository):

    def send_email(self, subject: str, content: str) -> None:
        message = Mail(
            from_email=settings.EMAIL_FROM,
            to_emails=settings.EMAIL_TO,
            subject=subject,
            html_content=content
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            sg.send(message)
        except Exception as e:
            raise Exception(f"Error enviando email: {str(e)}")
