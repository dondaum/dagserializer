import uuid
from functools import wraps


def dbt_manifest_version() -> list:
    """
    Function that returns all manifest versions
    that shall be tested
    """
    return [
        'manifest_0.19.2.json',
        'manifest_0.20.0.json',
        'manifest_0.21.0.json',
    ]


DBT_MANIFEST_SCHEMAS = {
    "v1": {
        "nodes": {},
        "sources": {},
        "macros": {},
        "exposures": {},
        "metrics": {},
        "selectors": {},
        "parent_map": {},
        "child_map": {},
        "docs": {},
        "metadata": {
            "generated_at": "2018-02-14T09:15:13Z",
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v1.json",
            "dbt_version": "0.19.2",
            "project_id": uuid.uuid4().hex,
            "user_id": "cfc4500f-dc7f-4c63-9ea7-2c582c1b38cf",
            "send_anonymous_usage_stats": False,
            "adapter_type": "postgres",
            "invocation_id": uuid.uuid4().hex,
            "env": {},
        },
        "disabled": [],
    },
    "v4": {
        "nodes": {},
        "sources": {},
        "macros": {},
        "exposures": {},
        "metrics": {},
        "selectors": {},
        "parent_map": {},
        "child_map": {},
        "docs": {},
        "metadata": {
            "generated_at": "2018-02-14T09:15:13Z",
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v4.json",
            "dbt_version": "0.19.2",
            "project_id": uuid.uuid4().hex,
            "user_id": "cfc4500f-dc7f-4c63-9ea7-2c582c1b38cf",
            "send_anonymous_usage_stats": False,
            "adapter_type": "postgres",
            "invocation_id": uuid.uuid4().hex,
            "env": {},
        },
        "disabled": {},
    },
}


def get_manifest_version(manifest_version: str):
    """
    Decorator that returns the correct dbt manifest schema
    version
    """

    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_manifest_version = "manifest_version"
            kwargs[arg_manifest_version] = DBT_MANIFEST_SCHEMAS[
                manifest_version
            ]
            return func(*args, **kwargs)

        return wrapper

    return inner_func
