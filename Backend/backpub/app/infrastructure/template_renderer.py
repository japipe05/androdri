from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path


class TemplateRenderer:
    def __init__(self):
        template_path = Path(__file__).resolve().parent.parent / "templates"

        self.env = Environment(
            loader=FileSystemLoader(template_path),
            autoescape=select_autoescape(["html", "xml"])
        )

    def render(self, template_name: str, context: dict) -> str:
        template = self.env.get_template(template_name)
        return template.render(**context)
