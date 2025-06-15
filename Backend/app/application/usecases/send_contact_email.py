from app.domain.models import ContactForm
from app.ports.email_port import EmailPort

class SendContactEmail:
    def __init__(self, email_service: EmailPort):
        self.email_service = email_service

    def execute(self, contact: ContactForm):
        self.email_service.send(contact)
