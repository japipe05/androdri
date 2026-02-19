"""
===============================================================================
Archivo:        token_model.py
Ubicación:      app/models/token_model.py
Descripción:    Define los modelos de datos utilizados para la autenticación
                mediante tokens. Contiene las estructuras para las solicitudes
                de generación de token y las respuestas entregadas por el
                sistema de autenticación.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0004af
===============================================================================
"""

from pydantic import BaseModel


class TokenRequest(BaseModel):
    """
    Modelo de solicitud para la generación de un token de acceso.

    Este modelo valida la información enviada por el cliente que desea obtener
    un token de autenticación (por ejemplo, un API Key). Puede ser usado en un
    endpoint del tipo `/token` o `/auth/login`.

    Atributos
    ---------
    api_key : str
        Clave de autenticación proporcionada al cliente para solicitar un token.
    """

    api_key: str


class TokenResponse(BaseModel):
    """
    Modelo de respuesta que contiene la información del token emitido.

    Este modelo representa el cuerpo de la respuesta devuelta por el servidor
    una vez autenticado el cliente de manera correcta. Generalmente se incluye
    el token de acceso y su tipo, utilizado en los encabezados de futuras
    solicitudes protegidas (`Authorization: Bearer <token>`).

    Atributos
    ---------
    access_token : str
        Token JWT o similar que autoriza al cliente a acceder a los endpoints protegidos.
    token_type : str, opcional
        Tipo de token (por defecto, "bearer").
    """

    access_token: str
    token_type: str = "bearer"
