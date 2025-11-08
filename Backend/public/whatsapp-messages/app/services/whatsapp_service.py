"""
===============================================================================
Archivo:        whatsapp_service.py
Ubicación:      app/services/whatsapp_service.py
Descripción:    Implementa el servicio responsable de enviar mensajes de WhatsApp
                utilizando la API de Twilio (si está configurada). En caso de no
                contar con credenciales válidas, el servicio entra en modo 
                simulación (mock) para entornos de desarrollo o pruebas.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0004af
===============================================================================
"""

from typing import Dict
from fastapi import HTTPException, status
from app.config.settings import settings

# --------------------------------------------------------------------------
# Importación condicional del cliente Twilio
# Si no existen las dependencias o credenciales, el sistema usa un simulador.
# --------------------------------------------------------------------------
try:
    from twilio.rest import Client
except Exception:
    Client = None


# --------------------------------------------------------------------------
# Clase principal del servicio de mensajería WhatsApp
# --------------------------------------------------------------------------
class WhatsAppService:
    """
    Servicio encargado de enviar mensajes de WhatsApp.

    ### Funcionalidad principal
    - Permite enviar mensajes a través de la API de **Twilio WhatsApp** si las
      credenciales están configuradas en `settings`.
    - Si no se detecta configuración válida o el paquete Twilio no está instalado,
      entra en **modo simulado**, devolviendo una respuesta falsa útil para
      entornos de desarrollo o testing.

    ### Dependencias de configuración:
    - `TWILIO_ACCOUNT_SID`
    - `TWILIO_AUTH_TOKEN`
    - `TWILIO_WHATSAPP_NUMBER`
    """

    def __init__(self):
        """
        Inicializa el cliente de Twilio si las credenciales están disponibles.
        Si no, activa el modo de simulación.
        """
        if Client and settings.TWILIO_ACCOUNT_SID and settings.TWILIO_AUTH_TOKEN:
            self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        else:
            self.client = None

    # ----------------------------------------------------------------------
    # Método principal: envío de mensaje
    # ----------------------------------------------------------------------
    def send_message(self, to: str, body: str) -> Dict:
        """
        Envía un mensaje de WhatsApp al número indicado.

        ### Parámetros
        - **to** (`str`): Número de destino, con código de país (ejemplo: `+573001234567`).
        - **body** (`str`): Texto del mensaje a enviar.

        ### Retorna
        - `Dict`: Objeto con información del mensaje enviado o simulado:
          ```json
          {
              "sid": "SMxxxxxxxx",
              "status": "sent"
          }
          ```

        ### Flujo de ejecución
        1. Valida el formato del número (`to` debe comenzar con `+`).
        2. Si el cliente Twilio está configurado:
           - Envía el mensaje real a través de la API de Twilio.
           - Retorna el SID y estado.
        3. Si no hay configuración Twilio:
           - Devuelve un resultado simulado (modo local/test).

        ### Errores posibles
        - **400 Bad Request**: Si el número no comienza con `+`.
        - **500 Internal Server Error**: Si ocurre un error al comunicarse con Twilio.

        ### Ejemplo de uso
        ```python
        from app.services.whatsapp_service import whatsapp_service

        result = whatsapp_service.send_message("+573001234567", "Hola desde FastAPI 🚀")
        print(result)
        ```
        """
        # Validación del formato básico del número de teléfono
        if not to.startswith("+"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="phone_number must start with + and country code"
            )

        # Envío real mediante Twilio (si está configurado)
        if self.client:
            from_number = f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}"
            to_number = f"whatsapp:{to}"
            try:
                message = self.client.messages.create(
                    body=body,
                    from_=from_number,
                    to=to_number
                )
                return {"sid": message.sid, "status": message.status}
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"provider error: {e}"
                )

        # Fallback: modo simulado (útil en desarrollo)
        return {
            "sid": "SIMULATED-1234",
            "status": "sent",
            "to": to,
            "body": body
        }


# --------------------------------------------------------------------------
# Instancia global del servicio (Singleton Pattern)
# --------------------------------------------------------------------------
whatsapp_service = WhatsAppService()
