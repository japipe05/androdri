from app.domain.entities import Email
from app.infrastructure.email.html_renderer import HtmlEmailRenderer


def make_email(**kw) -> Email:
    data = dict(receptor="a@b.com", emisor="x@Androdri.com", asunto="Hola", mensaje="Mensaje")
    return Email(**{**data, **kw})


def test_subject_and_body_have_emojis_and_html():
    rendered = HtmlEmailRenderer("Androdri").render(make_email())
    assert rendered.subject.startswith("📬")
    assert "<html" in rendered.html and "📬" in rendered.html and "💬" in rendered.html
    assert "✨" in rendered.text


def test_message_is_html_escaped():
    rendered = HtmlEmailRenderer("Androdri").render(
        make_email(mensaje="<script>alert(1)</script>", asunto="<b>x</b>")
    )
    assert "<script>" not in rendered.html
    assert "&lt;script&gt;" in rendered.html
    assert "<b>x</b>" not in rendered.html


def test_line_breaks_become_br():
    rendered = HtmlEmailRenderer("Androdri").render(make_email(mensaje="uno\ndos"))
    assert "uno<br>dos" in rendered.html
