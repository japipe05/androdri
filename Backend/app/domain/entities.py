from dataclasses import dataclass

from app.domain.exceptions import InvalidEmailError


@dataclass(frozen=True, slots=True)
class Email:
    """Entidad de dominio: un correo a enviar."""

    receptor: str
    emisor: str
    asunto: str
    mensaje: str

    def __post_init__(self) -> None:
        # Previene inyección de cabeceras (header injection).
        for name in ("receptor", "emisor", "asunto"):
            if any(ch in getattr(self, name) for ch in ("\r", "\n")):
                raise InvalidEmailError(f"El campo '{name}' no puede contener saltos de línea.")
        if not self.asunto.strip():
            raise InvalidEmailError("El asunto no puede estar vacío.")
        if not self.mensaje.strip():
            raise InvalidEmailError("El mensaje no puede estar vacío.")

    @property
    def emisor_domain(self) -> str:
        return self.emisor.rsplit("@", 1)[-1].lower()


@dataclass(frozen=True, slots=True)
class RenderedEmail:
    """Resultado de renderizar un Email: asunto con emojis + HTML + texto plano."""

    subject: str
    html: str
    text: str
