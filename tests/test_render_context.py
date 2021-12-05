import os
import unittest
from os import path
from tempfile import TemporaryDirectory

from dagserializer import logger
from dagserializer.jinja_render_context import JinjaRenderContext


class RenderContextTest(unittest.TestCase):
    def setUp(self):
        logger.init_logger()
        self.template_dir = TemporaryDirectory()

    def tearDown(self):
        logger.logger = None
        self.template_dir.cleanup()

    def template(self) -> str:
        """
        Method that returns a dummy jinja template as str
        """
        return """models ->{{ models }}"""

    def test_get_template(self):
        """
        Method that test if a template directory and jinja
        template can be passed as args and return as jinja
        Template
        """
        template = self.template()
        target_path = path.join(self.template_dir.name, 'test.jinja2')
        with open(target_path, 'w') as fp:
            fp.write(template)
        renderer = JinjaRenderContext(template_dir=self.template_dir.name)
        templ = renderer.get_template('test.jinja2')
        rendered = templ.render({'models': ['a', 'b']})
        self.assertEqual(rendered, """models ->['a', 'b']""")
