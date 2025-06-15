from abc import ABC, abstractmethod
from app.domain.models import ContactForm

class EmailPort(ABC):
    @abstractmethod
    def send(self, contact: ContactForm) -> None:
        pass
