import io
import zipfile
from typing import List, Tuple, Optional

def create_zip(files: List[Tuple[str, bytes]], password: Optional[str] = None) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for filename, content in files:
            info = zipfile.ZipInfo(filename)
            if password:
                # Solo ZipCrypto, inseguro pero compatible con Windows Explorer
                zf.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED)
                zf.setpassword(password.encode("utf-8"))
            else:
                zf.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED)
    buf.seek(0)
    return buf.read()
