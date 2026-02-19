from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from jinja2 import Environment, FileSystemLoader
from app.core.config import settings
from fastapi import HTTPException

env = Environment(loader=FileSystemLoader("app/templates"))

async def send_contact_email(data: dict):
    try:
        template = env.get_template("contact.html")
        html_content = template.render(**data)

        message = Mail(
            from_email=settings.EMAIL_FROM,
            to_emails=settings.EMAIL_TO,
            subject="📩 Nuevo mensaje desde la web",
            html_content=html_content,
        )

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)

        if response.status_code >= 400:
            raise Exception(response.body.decode())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Email error: {str(e)}")
