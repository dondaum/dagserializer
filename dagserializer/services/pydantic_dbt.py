import json
from importlib import import_module
from pathlib import Path
from typing import Union

import dagserializer.logger as log
from dagserializer.dbtschematas.v1 import Model as DbtModelV1
from dagserializer.dbtschematas.v2 import Model as DbtModelV2
from dagserializer.dbtschematas.v3 import Model as DbtModelV3
from dagserializer.dbtschematas.v4 import Model as DbtModelV4


def factory_load_dbt(
    dbt_manifest: dict,
) -> Union[DbtModelV1, DbtModelV2, DbtModelV3, DbtModelV4]:
    """
    Function that load pydantic models from a dbt
    manifest file
    """
    PYDDBT_FACTORY = {
        "https://schemas.getdbt.com/dbt/manifest/v1.json": DbtModelV1,
        "https://schemas.getdbt.com/dbt/manifest/v2.json": DbtModelV2,
        "https://schemas.getdbt.com/dbt/manifest/v3.json": DbtModelV3,
        "https://schemas.getdbt.com/dbt/manifest/v4.json": DbtModelV4,
    }

    dbt_manifest_version = dbt_manifest["metadata"]["dbt_schema_version"]
    factory_model = PYDDBT_FACTORY[dbt_manifest_version]
    log.logger.info(
        f"Running with dbt manifest version: {dbt_manifest_version}"
    )
    log.logger.info(f"Using factory class {factory_model}")
    return factory_model(**dbt_manifest)


def load_manifest_from(
    path: str,
) -> Union[DbtModelV1, DbtModelV2, DbtModelV3, DbtModelV4]:
    """
    Function that opens a manifest json and returns the pydantic
    model representations
    """
    full_path: Path = Path(path)
    with open(full_path) as file:
        raw_manifest = json.load(file)
    return factory_load_dbt(raw_manifest)
