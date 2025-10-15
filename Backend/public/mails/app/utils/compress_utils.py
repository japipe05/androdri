import os
import pyzipper
from tempfile import NamedTemporaryFile

def compress_files(files, password: str = None):
    """
    Comprime archivos y, si se indica, los cifra con AES256.
    Compatible con Windows, Android, macOS, iPhone (WinRAR, 7zip, etc.)
    """
    temp_zip = NamedTemporaryFile(delete=False, suffix=".zip")

    with pyzipper.AESZipFile(temp_zip, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:
        if password:
            zipf.setpassword(password.encode())
            zipf.setencryption(pyzipper.WZ_AES, nbits=256)

        for file in files:
            file.file.seek(0)
            data = file.file.read()
            zipf.writestr(file.filename, data)

    return temp_zip.name
