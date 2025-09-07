from app.models.contact_model import ContactRequest, ContactResponse
from app.utils.email_sender import send_email
from app.utils.exceptions import EmailSendError


def process_contact(contact: ContactRequest) -> ContactResponse:
    """
    Procesa el contacto recibido y envía un correo electrónico.
    Lanza EmailSendError si ocurre un problema en el envío.
    """
    subject = f"Nuevo mensaje de {contact.name}"
    body = f"""
    Nombre: {contact.name}
    Email: {contact.email}
    Mensaje: {contact.message}
    """

    try:
        send_email(subject, body, contact.email)
        return ContactResponse(
            status="success",
            message="Mensaje enviado correctamente"
        )
    except Exception as e:
        # Si ocurre un error en el envío, lo controlamos con nuestra excepción custom
        raise EmailSendError(detail=f"No se pudo enviar el correo: {str(e)}")
