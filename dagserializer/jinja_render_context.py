from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template

from dagserializer.contracts.render_context import RenderContext


class JinjaRenderContext(RenderContext):
    """
    Class that implements the RenderContext contracts and is
    responsible for providing jinja templating functionalities
    """

    def __init__(self, template_dir: Path) -> None:
        self.template_dir = template_dir
        super().__init__()

    def get_template(self, template_file_path: Path) -> Template:
        """
        Method that expects a template file path and returns a jinja
        environment
        """
        str_path = str(template_file_path)
        loader = FileSystemLoader(str(self.template_dir))
        environment = Environment(loader=loader)
        return environment.get_template(str_path)
