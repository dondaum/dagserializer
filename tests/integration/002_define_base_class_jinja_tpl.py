import unittest

from dagserializer import logger


class RenderPydDbtContextTest(unittest.TestCase):
    def setUp(self):
        logger.init_logger()

    def tearDown(self):
        logger.logger = None

    def test_jinja_render_pyddbt_context(self):
        """
        Method that test if pydantic dbt representation
        can be make availabe for jinja rendering
        """
        pass
