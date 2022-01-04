from abc import ABC, abstractmethod
from pprint import pprint
from typing import Dict, Optional, Union

from dagserializer.contracts.render_context import RenderContext
from dagserializer.dbtschematas.v1 import (
    CompiledModelNode as CompiledModelNodeV1,
)
from dagserializer.dbtschematas.v1 import Model as DbtModelV1
from dagserializer.dbtschematas.v1 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV1,
)
from dagserializer.dbtschematas.v2 import (
    CompiledModelNode as CompiledModelNodeV2,
)
from dagserializer.dbtschematas.v2 import Model as DbtModelV2
from dagserializer.dbtschematas.v2 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV2,
)
from dagserializer.dbtschematas.v3 import (
    CompiledModelNode as CompiledModelNodeV3,
)
from dagserializer.dbtschematas.v3 import Model as DbtModelV3
from dagserializer.dbtschematas.v3 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV3,
)
from dagserializer.dbtschematas.v4 import (
    CompiledModelNode as CompiledModelNodeV4,
)
from dagserializer.dbtschematas.v4 import Model as DbtModelV4
from dagserializer.dbtschematas.v4 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV4,
)
from dagserializer.services.pydantic_dbt import load_manifest_from


class BaseGenerator(ABC):
    """
    Base class for defining the interface that Generator
    implementation must implement.
    """

    def __init__(self, dbt_manifest_path: str, renderer: RenderContext) -> None:
        self.dbt_manifest_path = dbt_manifest_path
        self.renderer = renderer

        self.pyd_dbt_manifest: Optional[
            Union[DbtModelV1, DbtModelV2, DbtModelV3, DbtModelV4]
        ] = None

    def load_manifest(
        self,
    ) -> Union[DbtModelV1, DbtModelV2, DbtModelV3, DbtModelV4]:
        """
        Method that load a pydantic representation of the dbt manfifest
        """
        if self.pyd_dbt_manifest:
            return self.pyd_dbt_manifest
        self.pyd_dbt_manifest = load_manifest_from(self.dbt_manifest_path)
        return self.pyd_dbt_manifest

    def extract_models(
        self,
    ) -> Dict[
        str,
        Union[
            CompiledModelNodeV1,
            CompiledModelNodeV2,
            CompiledModelNodeV3,
            CompiledModelNodeV4,
        ],
    ]:
        """
        Method that returns all dbt models
        """
        if not self.pyd_dbt_manifest:
            return {}
        return {
            k: v
            for (k, v) in self.pyd_dbt_manifest.nodes.items()
            if 'CompiledModelNode' in v.__class__.__name__
        }

    def extract_sources(
        self,
    ) -> Dict[
        str,
        Union[
            ParsedSourceDefinitionV1,
            ParsedSourceDefinitionV2,
            ParsedSourceDefinitionV3,
            ParsedSourceDefinitionV4,
        ],
    ]:
        """
        Method that returns all dbt sources
        """
        if not self.pyd_dbt_manifest:
            return {}
        return {
            k: v
            for (k, v) in self.pyd_dbt_manifest.sources.items()
            if 'ParsedSourceDefinition' in v.__class__.__name__
        }

    def show_model_dependencies(self) -> None:
        """
        Util method that only prints out models and depdencies with
        plain Python objects sorted by dependencies
        """
        display = {}
        extr_models = self.extract_models()
        for name, model in extr_models.items():
            display[name] = model.depends_on.nodes  # type: ignore
        sort_disply = sorted(display.items(), key=lambda kv: (len(kv[1]), kv[0]))  # type: ignore
        pprint(sort_disply)

    @abstractmethod
    def render_dag(self):
        pass
