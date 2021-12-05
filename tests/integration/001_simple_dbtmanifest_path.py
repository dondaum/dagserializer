import unittest

from dagserializer import logger
from dagserializer.services.pydantic_dbt import factory_load_dbt
from tests.utils import get_manifest_version


class DbtManifestPathTest(unittest.TestCase):
    def setUp(self):
        logger.init_logger()

    def tearDown(self):
        logger.logger = None

    def test_dummy(self):
        """
        Method that test if a dbt manifest.json artifact
        can translated in pydantic models from a factory function
        """
        pass
