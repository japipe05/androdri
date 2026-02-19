import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition
)
from jinja2 import Environment, FileSystemLoader
from app.config.settings import settings


class EmailService:
    def __init__(self):
        self.sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        self.templates = Environment(
            loader=FileSystemLoader("app/templates")
        )

    def send_email(self, asunto, mensaje, archivos, comprimir, password):
        template = self.templates.get_template("email_template.html")
        html_content = template.render(
            mensaje=mensaje,
            version=settings.APP_VERSION
        )

        message = Mail(
            from_email=(settings.SENDGRID_FROM_EMAIL, settings.SENDGRID_FROM_NAME),
            to_emails=settings.SENDGRID_FROM_EMAIL,
            subject=f"📬 {asunto} - FastAPI Androdri",
            html_content=html_content
        )

        if archivos:
            for file in archivos:
                encoded = base64.b64encode(file.file.read()).decode()
                attachment = Attachment(
                    FileContent(encoded),
                    FileName(file.filename),
                    FileType("application/octet-stream"),
                    Disposition("attachment")
                )
                message.add_attachment(attachment)

        response = self.sg.send(message)

        if response.status_code not in (200, 202):
            raise Exception(
                f"SendGrid error {response.status_code}: {response.body}"
            )
