import os

from dagserializer.generator.base import BaseGenerator
from dagserializer.jinja_render_context import JinjaRenderContext


class SimpleDagGenerator(BaseGenerator):
    def __init__(
        self, dbt_manifest_path: str, renderer: JinjaRenderContext
    ) -> None:
        super().__init__(dbt_manifest_path, renderer)

    def render_dag(self):
        template = self.renderer.get_template('airflow_dag_template_1.jinja2')
        dag = template.render({'pyd_dbt_model': self.load_manifest()})
        here = os.path.dirname(os.path.abspath(__file__))
        with open(
            os.path.join(here, '../output/airflow_dag_template_1.py'), 'w'
        ) as f:
            f.write(dag)
