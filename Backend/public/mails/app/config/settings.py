"""
===============================================================================
Archivo:        settings.py
Ubicación:      app/config/settings.py
Descripción:    Configuración central de la aplicación FastAPI. Define y carga
                las variables de entorno utilizando Pydantic Settings para
                asegurar validación, tipado estricto y fácil acceso a los
                parámetros de configuración en toda la aplicación.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0002af
===============================================================================
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """
    Clase principal de configuración para la aplicación FastAPI.

    Esta clase utiliza `pydantic_settings.BaseSettings` para mapear y validar
    automáticamente las variables de entorno definidas en un archivo `.env` o
    directamente en el entorno del sistema operativo.  
    Proporciona acceso centralizado a todos los parámetros de configuración
    relevantes de la aplicación.

    Atributos
    ---------
    APP_NAME : str
        Nombre de la aplicación.
    APP_VERSION : str
        Versión actual del despliegue o build.
    APP_DESCRIPTION : str
        Descripción general de la aplicación.
    APP_FECHAMOD : str
        Fecha de la última modificación del proyecto.

    ALLOWED_ORIGINS : List[str]
        Lista de dominios permitidos para solicitudes CORS.

    SMTP_HOST : str
        Servidor de correo saliente (SMTP).
    SMTP_PORT : int
        Puerto asociado al servidor SMTP.
    SMTP_USER : str
        Usuario autenticado para el servicio de correo.
    SMTP_PASSWORD : str
        Contraseña del usuario SMTP (se recomienda mantenerla en secreto en el .env).

    JWT_SECRET_KEY : str
        Clave secreta utilizada para la generación y validación de tokens JWT.
    PORT : int
        Puerto en el que se ejecutará la aplicación FastAPI.
    """

    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_FECHAMOD: str

    ALLOWED_ORIGINS: List[str]

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str

    JWT_SECRET_KEY: str
    PORT: int

    class Config:
        """
        Configuración interna de Pydantic Settings.

        Especifica la ruta y codificación del archivo `.env` desde donde se
        cargarán las variables de entorno. Esto permite centralizar la
        configuración y mantener credenciales fuera del código fuente.
        """
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instancia global de configuración
# -------------------------------------------------------------------------------
# Esta instancia se crea una sola vez y puede ser importada en cualquier parte
# de la aplicación mediante:
#   >>> from app.config.settings import settings
# lo que garantiza un acceso rápido y consistente a los valores configurados.
# -------------------------------------------------------------------------------
settings = Settings()
