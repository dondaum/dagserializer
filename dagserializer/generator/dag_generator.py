from typing import Dict, List, Optional, Tuple, Union

from dagserializer.contracts.render_context import RenderContext
from dagserializer.custom_types import (
    GenericCompiledModelNode,
    GenericDbtModel,
    GenericParsedSourceDefinition,
)
from dagserializer.generator.base import BaseGenerator


class DagGenerator(BaseGenerator):
    """
    Dag Generator class that creates objects from dbt manifest that
    can be easly used to create an Airflow like DAG

    dbt_manifest_path: Path location of the dbt manifest
    renderer: Renderer Context base object
    has_dbt_source_check: If dbt sources shall be handled as airflow tasks on which dbt models can depend on
    """

    def __init__(
        self,
        dbt_manifest_path: str,
        renderer: RenderContext,
        has_dbt_source_check=True,
    ) -> None:
        self.has_dbt_source_check = has_dbt_source_check
        super().__init__(dbt_manifest_path, renderer)

    def generate_airflow_tasks(
        self,
    ) -> Tuple[
        Union[
            GenericDbtModel,
            GenericCompiledModelNode,
            GenericParsedSourceDefinition,
        ]
    ]:
        models = self.extract_models()
        return models

    def get_parent_map(self) -> Optional[Optional[Dict[str, List[str]]]]:
        dbt_model = self.load_manifest()
        return {
            model: dbt_model.parent_map[model]
            for model in dbt_model.parent_map
            if model.split(".")[0] == 'model'
        }
        # return dbt_model.parent_map

    def render_dag(self):
        pass
