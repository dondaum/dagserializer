from abc import ABC, abstractmethod
from pprint import pprint
from typing import Dict, Optional, Union

from dagserializer.contracts.render_context import RenderContext
from dagserializer.custom_types import (
    GenericCompiledModelNode,
    GenericDbtModel,
    GenericParsedSourceDefinition,
)
from dagserializer.dbtschematas.v1 import (
    CompiledModelNode as CompiledModelNodeV1,
)
from dagserializer.dbtschematas.v1 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV1,
)
from dagserializer.dbtschematas.v2 import (
    CompiledModelNode as CompiledModelNodeV2,
)
from dagserializer.dbtschematas.v2 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV2,
)
from dagserializer.dbtschematas.v3 import (
    CompiledModelNode as CompiledModelNodeV3,
)
from dagserializer.dbtschematas.v3 import (
    ParsedSourceDefinition as ParsedSourceDefinitionV3,
)
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

        self.pyd_dbt_manifest: Optional[GenericDbtModel] = None

    def load_manifest(
        self,
    ) -> GenericDbtModel:
        """
        Method that load a pydantic representation of the dbt manfifest
        """
        if self.pyd_dbt_manifest:
            return self.pyd_dbt_manifest
        self.pyd_dbt_manifest = load_manifest_from(self.dbt_manifest_path)
        return self.pyd_dbt_manifest

    def extract_models(
        self,
    ) -> Dict[str, GenericCompiledModelNode]:
        """
        Method that returns all dbt models
        """
        comp_models_typed = (
            CompiledModelNodeV1,
            CompiledModelNodeV2,
            CompiledModelNodeV3,
        )
        if not self.pyd_dbt_manifest:
            return {}
        return {
            k: v
            for (k, v) in self.pyd_dbt_manifest.nodes.items()
            if isinstance(v, comp_models_typed)
        }

    def extract_sources(
        self,
    ) -> Dict[str, GenericParsedSourceDefinition]:
        """
        Method that returns all dbt sources
        """
        comp_source_typed = (
            ParsedSourceDefinitionV1,
            ParsedSourceDefinitionV2,
            ParsedSourceDefinitionV3,
            ParsedSourceDefinitionV4,
        )
        if not self.pyd_dbt_manifest:
            return {}
        return {
            k: v
            for (k, v) in self.pyd_dbt_manifest.sources.items()
            if isinstance(v, comp_source_typed)
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
