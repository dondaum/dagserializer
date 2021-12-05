import os
import unittest

from dagserializer import logger
from dagserializer.services.pydantic_dbt import (
    factory_load_dbt,
    load_manifest_from,
)
from tests.data import DATA_PATH
from tests.utils import get_manifest_version


class PydanticDbtTest(unittest.TestCase):
    def setUp(self):
        logger.init_logger()

    def tearDown(self):
        logger.logger = None

    @get_manifest_version("v4")
    def test_if_pydantic_factory_loads_models(self, manifest_version):
        """
        Method that test if a dbt manifest.json artifact
        can translated in pydantic models from a factory function
        """
        dbt_manifest = manifest_version
        pyd = factory_load_dbt(dbt_manifest=dbt_manifest)
        self.assertIsNotNone(pyd)

    def test_load_manifest_from(self):
        """
        Method that test if a dbt manifest.json artifact
        can translated in pydantic models from a factory function
        """
        target_path = os.path.join(DATA_PATH, 'manifest_0.19.2.json')
        pyd = load_manifest_from(target_path)
        self.assertIsNotNone(pyd)
