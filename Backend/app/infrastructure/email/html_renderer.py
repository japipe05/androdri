from html import escape
from string import Template

from app.domain.entities import Email, RenderedEmail

_HTML_TEMPLATE = Template(
    """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$subject</title>
</head>
<body style="margin:0;padding:0;background-color:#f4f6f8;font-family:Arial,Helvetica,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
         style="background-color:#f4f6f8;padding:24px 0;">
    <tr><td align="center">
      <table role="presentation" width="600" cellspacing="0" cellpadding="0"
             style="max-width:600px;width:100%;background:#ffffff;border-radius:12px;overflow:hidden;">
        <tr>
          <td style="background:#1f6feb;color:#ffffff;padding:24px;text-align:center;">
            <div style="font-size:40px;">📬</div>
            <h1 style="margin:8px 0 0;font-size:22px;">✨ $subject</h1>
          </td>
        </tr>
        <tr>
          <td style="padding:28px;color:#333333;font-size:16px;line-height:1.6;">
            💬 $message
          </td>
        </tr>
        <tr>
          <td style="padding:16px 28px;background:#fafbfc;color:#777777;font-size:13px;text-align:center;">
            🚀 Enviado con 💙 desde $brand Contactanos
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""
)


class HtmlEmailRenderer:
    """Renderiza asunto con emoji + cuerpo HTML (escapado) + alternativa en texto plano."""

    def __init__(self, brand_name: str) -> None:
        self._brand = brand_name

    def render(self, email: Email) -> RenderedEmail:
        message = email.mensaje.replace("\r\n", "\n").replace("\r", "\n")

        # escape() evita inyección de HTML/JS en el cuerpo del correo.
        html = _HTML_TEMPLATE.substitute(
            subject=escape(email.asunto),
            message=escape(message).replace("\n", "<br>"),
            brand=escape(self._brand),
        )
        text = f"✨ {email.asunto}\n\n💬 {message}\n\n🚀 Enviado con 💙 desde {self._brand} Contactanos"
        return RenderedEmail(subject=f"📬 Contactanos: {email.asunto}", html=html, text=text)
