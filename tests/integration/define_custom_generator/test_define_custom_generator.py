import os
import unittest

from dagserializer import logger
from dagserializer.jinja_render_context import JinjaRenderContext
from tests.data import DATA_PATH
from tests.integration.define_custom_generator.generator.simple_dag_generator import (
    SimpleDagGenerator,
)


class CustomerGeneratorIntTest(unittest.TestCase):
    def setUp(self):
        logger.init_logger()

    def tearDown(self):
        logger.logger = None

    def test_if_dag_file_can_be_rendered(self):
        """
        Method that that defines templates, a custom generator
        and test if a DAG file is rendered
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(cur, 'templates')
        manifest_path = os.path.join(DATA_PATH, 'manifest_0.19.2.json')
        jinja = JinjaRenderContext(template_dir)
        gen = SimpleDagGenerator(
            dbt_manifest_path=manifest_path,
            renderer=jinja,
        )
        gen.render_dag()
        here = os.path.dirname(os.path.abspath(__file__))
        dag_file = os.path.join(here, 'output/airflow_dag_template_1.py')
        with open(dag_file) as file:
            dag = file.readlines()

        try:
            os.remove(dag_file)
        except OSError:
            pass

        self.assertIsNotNone(dag)
