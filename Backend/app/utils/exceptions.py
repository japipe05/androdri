from fastapi import HTTPException, status


class EmailSendError(HTTPException):
    def __init__(self, detail: str = "Error al enviar el correo"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class InvalidContactError(HTTPException):
    def __init__(self, detail: str = "Datos de contacto inválidos"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
