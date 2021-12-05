from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template


def get_template(template_file_path: Path) -> Template:
    loader = FileSystemLoader(str(TEMPLATE_DIR / template_file_path.parent))
    environment: Environment = Environment(loader=loader)
    return environment.get_template(template_file_path.name)
