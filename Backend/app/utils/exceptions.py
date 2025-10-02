from fastapi import HTTPException, status

class EmailSendException(HTTPException):
    def __init__(self, detail="Error enviando el correo"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class AttachmentTooLargeException(HTTPException):
    def __init__(self, detail="Adjunto demasiado grande"):
        super().__init__(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail=detail)
