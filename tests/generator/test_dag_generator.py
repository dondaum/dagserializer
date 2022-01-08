import os
import unittest

from parameterized import parameterized

from dagserializer.generator.dag_generator import DagGenerator
from tests.data import DATA_PATH
from tests.generator.test_base import DummyRenderContext
from tests.utils import dbt_manifest_version


class DagGeneratorTest(unittest.TestCase):
    def test_init(self):
        """
        Test init of dag generator class with params
        """
        gen = DagGenerator(
            dbt_manifest_path="xzx/asdsa/zxck/manifest.json",
            renderer=DummyRenderContext(),
        )
        self.assertIsNotNone(gen)
        self.assertEqual(gen.has_dbt_source_check, True)

    @parameterized.expand(dbt_manifest_version())
    def test_load_manifest(self, manifest):
        """
        Test if manifest can be loaded
        """
        target_path = os.path.join(DATA_PATH, manifest)
        gen = DagGenerator(
            dbt_manifest_path=target_path, renderer=DummyRenderContext()
        )
        self.assertIsNone(gen.get_parent_map())


if __name__ == "__main__":
    unittest.main()
