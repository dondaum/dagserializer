from typing import Union

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

GenericDbtModel = Union[DbtModelV1, DbtModelV2, DbtModelV3, DbtModelV4]
GenericCompiledModelNode = Union[
    CompiledModelNodeV1,
    CompiledModelNodeV2,
    CompiledModelNodeV3,
    CompiledModelNodeV4,
]
GenericParsedSourceDefinition = Union[
    ParsedSourceDefinitionV1,
    ParsedSourceDefinitionV2,
    ParsedSourceDefinitionV3,
    ParsedSourceDefinitionV4,
]
