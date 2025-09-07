from fastapi import APIRouter, status, Depends
from app.models.contact_model import ContactRequest, ContactResponse
from app.services.contact_service import process_contact
from app.utils.security import get_current_user

router = APIRouter(prefix="/api/contact/v1", tags=["Contact"])

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_200_OK)
def send_contact(contact: ContactRequest, user=Depends(get_current_user)):
    """
    Solo se procesa el contacto si el token JWT es válido.
    """
    # user contiene el payload del JWT
    return process_contact(contact)
