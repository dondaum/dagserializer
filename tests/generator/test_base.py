import os
import unittest
from unittest.mock import patch
from pathlib import Path

from parameterized import parameterized

from dagserializer.contracts.render_context import RenderContext
from dagserializer.generator.base import BaseGenerator
from tests.data import DATA_PATH
from tests.utils import dbt_manifest_version


class DummyRenderContext(RenderContext):
    def get_template(
        self,
        template_file_path: Path,
    ) -> None:
        pass


class FakeGenerator(BaseGenerator):
    def __init__(self, dbt_manifest_path: str, renderer: RenderContext) -> None:
        super().__init__(dbt_manifest_path, renderer)

    def render_dag(self):
        pass


class FakeGeneratorTest(unittest.TestCase):
    def get_expected_models(self) -> list:
        """
        Method that returns the expected models
        """
        return [
            'model.ro_exemplar.order_items',
            'model.ro_exemplar.part_suppliers',
            'model.ro_exemplar.agg_customer_orders',
            'model.ro_exemplar.dim_customers',
            'model.ro_exemplar.dim_suppliers',
            'model.ro_exemplar.fct_order_items',
            'model.ro_exemplar.fct_orders',
            'model.ro_exemplar.dim_parts',
            'model.ro_exemplar.agg_ship_modes_hardcoded_pivot',
            'model.ro_exemplar.agg_regions_segments',
            'model.ro_exemplar.agg_ship_modes_dynamic_pivot',
            'model.ro_exemplar.stg_tpch_orders',
            'model.ro_exemplar.stg_tpch_nations',
            'model.ro_exemplar.stg_tpch_regions',
            'model.ro_exemplar.stg_tpch_customers',
            'model.ro_exemplar.stg_tpch_suppliers',
            'model.ro_exemplar.stg_tpch_parts',
            'model.ro_exemplar.stg_tpch_line_items',
            'model.ro_exemplar.stg_tpch_part_suppliers'
        ]

    def test_init(self):
        """
        Test init of base class with params
        """
        gen = FakeGenerator(
            dbt_manifest_path="xzx/asdsa/zxck/manifest.json",
            renderer=DummyRenderContext(),
        )
        self.assertIsNotNone(gen)

    @parameterized.expand(dbt_manifest_version())
    def test_load_manifest(self, manifest):
        """
        Test if manifest can be loaded
        """
        target_path = os.path.join(DATA_PATH, manifest)
        gen = FakeGenerator(
            dbt_manifest_path=target_path, renderer=DummyRenderContext()
        )
        self.assertIsNotNone(gen)

    @parameterized.expand(dbt_manifest_version())
    def test_extract_models(self, manifest):
        """
        Test if all nodes of type models can be extracted
        """
        target_path = os.path.join(DATA_PATH, manifest)
        gen = FakeGenerator(
            dbt_manifest_path=target_path, renderer=DummyRenderContext()
        )

        gen.load_manifest()
        models = gen.extract_models()
        self.assertEqual(list(models.keys()), self.get_expected_models())


    @parameterized.expand(dbt_manifest_version())
    def test_extract_sources(self, manifest):
        """
        Test if all nodes of type sources can be extracted
        """
        exp_sources = [
            'source.ro_exemplar.tpch.orders',
            'source.ro_exemplar.tpch.customer',
            'source.ro_exemplar.tpch.lineitem',
            'source.ro_exemplar.tpch.nation',
            'source.ro_exemplar.tpch.part',
            'source.ro_exemplar.tpch.partsupp',
            'source.ro_exemplar.tpch.region',
            'source.ro_exemplar.tpch.supplier'
        ]
        target_path = os.path.join(DATA_PATH, manifest)
        gen = FakeGenerator(
            dbt_manifest_path=target_path, renderer=DummyRenderContext()
        )

        gen.load_manifest()
        sources = gen.extract_sources()
        self.assertEqual(list(sources.keys()), exp_sources)

    @patch('dagserializer.generator.base.pprint')
    def test_show_model_dependencies(self, mock_pp):
        """
        Test if all model dependency are printed
        """
        target_path = os.path.join(DATA_PATH, 'manifest_0.19.2.json')
        gen = FakeGenerator(
            dbt_manifest_path=target_path, renderer=DummyRenderContext()
        )
        gen.load_manifest()
        gen.show_model_dependencies()
        mock_pp.assert_called()


if __name__ == "__main__":
    unittest.main()
