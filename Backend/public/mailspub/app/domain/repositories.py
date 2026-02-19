from abc import ABC, abstractmethod


class EmailRepository(ABC):
    @abstractmethod
    def send_email(self, subject: str, content: str) -> None:
        pass
