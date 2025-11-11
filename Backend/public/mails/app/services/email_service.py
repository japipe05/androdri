"""
===============================================================================
Archivo:        email_service.py
Ubicación:      app/services/email_service.py
Descripción:    Servicio encargado de la composición, renderización y envío de
                correos electrónicos. Permite adjuntar archivos, comprimirlos
                opcionalmente con cifrado AES y renderizar plantillas HTML
                mediante Jinja2. Utiliza configuración SMTP definida en settings.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0008af
===============================================================================
"""

import smtplib
import os
import tempfile
import pyzipper
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from app.config.settings import settings


class EmailService:
    """
    Servicio central de envío de correos electrónicos.

    Gestiona la creación del mensaje, renderización de contenido HTML,
    adjuntos (simples o comprimidos con contraseña) y conexión al servidor SMTP.

    Atributos
    ---------
    smtp_host : str
        Servidor SMTP utilizado para el envío de correos.
    smtp_port : int
        Puerto del servidor SMTP.
    smtp_user : str
        Usuario autenticado para el servicio SMTP.
    smtp_password : str
        Contraseña del usuario SMTP.
    templates : Environment
        Entorno Jinja2 para renderizar plantillas HTML de correo.
    """

    def __init__(self):
        """Inicializa los parámetros SMTP y carga las plantillas HTML."""
        self.smtp_host = settings.SMTP_HOST
        self.smtp_port = settings.SMTP_PORT
        self.smtp_user = settings.SMTP_USER
        self.smtp_password = settings.SMTP_PASSWORD

        # Configuración de entorno Jinja2
        self.templates = Environment(
            loader=FileSystemLoader("app/templates")
        )

    # -------------------------------------------------------------------------
    # MÉTODO PRINCIPAL DE ENVÍO
    # -------------------------------------------------------------------------
    def send_email(self, asunto, mensaje, archivos, comprimir, password):
        """
        Envía un correo electrónico utilizando los parámetros proporcionados.

        Parámetros
        ----------
        asunto : str
            Asunto del correo.
        mensaje : str
            Cuerpo principal del mensaje (texto o datos dinámicos).
        archivos : list[UploadFile] | None
            Lista de archivos adjuntos enviados desde el endpoint.
        comprimir : bool
            Indica si los archivos deben comprimirse en un ZIP antes de enviarse.
        password : str | None
            Contraseña opcional para proteger el archivo comprimido.

        Excepciones
        -----------
        smtplib.SMTPException
            Si ocurre un error al conectar o enviar el mensaje.
        """
        msg = EmailMessage()
        msg["Subject"] = f"📬 {asunto} - FastAPI Androdri"
        msg["From"] = self.smtp_user
        msg["To"] = self.smtp_user

        # ---------------------------------------------------------------------
        # Renderizar el contenido HTML con Jinja2
        # ---------------------------------------------------------------------
        template = self.templates.get_template("email_template.html")
        html_content = template.render(
            mensaje=mensaje,
            receptor=self.smtp_user,
            version=settings.APP_VERSION
        )
        msg.add_alternative(html_content, subtype="html")

        # ---------------------------------------------------------------------
        # Adjuntar archivos (directos o comprimidos)
        # ---------------------------------------------------------------------
        if archivos:
            if comprimir:
                zip_path = self._compress_files(archivos, password)
                with open(zip_path, "rb") as f:
                    msg.add_attachment(
                        f.read(),
                        maintype="application",
                        subtype="zip",
                        filename="archivos.zip"
                    )
                os.remove(zip_path)
            else:
                for file in archivos:
                    msg.add_attachment(
                        file.file.read(),
                        maintype="application",
                        subtype="octet-stream",
                        filename=file.filename
                    )

        # ---------------------------------------------------------------------
        # Envío del correo electrónico
        # ---------------------------------------------------------------------
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(self.smtp_user, self.smtp_password)
            smtp.send_message(msg)

    # -------------------------------------------------------------------------
    # MÉTODO AUXILIAR: COMPRESIÓN Y CIFRADO DE ARCHIVOS
    # -------------------------------------------------------------------------
    def _compress_files(self, archivos, password):
        """
        Comprime y opcionalmente cifra los archivos adjuntos en formato ZIP AES.

        Parámetros
        ----------
        archivos : list[UploadFile]
            Archivos a comprimir.
        password : str | None
            Contraseña opcional para proteger el archivo ZIP.

        Retorna
        -------
        str
            Ruta temporal del archivo ZIP generado.
        """
        zip_path = tempfile.mktemp(suffix=".zip")
        with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA) as zipf:
            if password:
                zipf.setpassword(password.encode())
                zipf.setencryption(pyzipper.WZ_AES, nbits=256)
            for file in archivos:
                zipf.writestr(file.filename, file.file.read())
        return zip_path
