import os
import re


TEST_CONFIG = """
    config: Optional[TestConfig] = {
        'enabled': True,
        'materialized': 'test',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': 'dbt_test__audit',
        'database': None,
        'tags': [],
        'full_refresh': None,
        'severity': 'ERROR',
        'store_failures': None,
        'where': None,
        'limit': None,
        'fail_calc': 'count(*)',
        'warn_if': '!= 0',
        'error_if': '!= 0',
        'post-hook': [],
        'pre-hook': [],
    }
"""

TEST_CONFIG_REPLACE = """
    config: Optional[TestConfig] = TestConfig(**{
        'enabled': True,
        'materialized': 'test',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': 'dbt_test__audit',
        'database': None,
        'tags': [],
        'full_refresh': None,
        'severity': 'ERROR',
        'store_failures': None,
        'where': None,
        'limit': None,
        'fail_calc': 'count(*)',
        'warn_if': '!= 0',
        'error_if': '!= 0',
        'post-hook': [],
        'pre-hook': [],
    })
"""


TEST_CONFIG_V2 = """
    config: Optional[TestConfig] = {
        'enabled': True,
        'alias': None,
        'schema': 'dbt_test__audit',
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'test',
        'severity': 'ERROR',
        'store_failures': None,
        'where': None,
        'limit': None,
        'fail_calc': 'count(*)',
        'warn_if': '!= 0',
        'error_if': '!= 0',
    }
"""

TEST_CONFIG_V2_REPLACE = """
    config: Optional[TestConfig] = TestConfig(**{
        'enabled': True,
        'alias': None,
        'schema': 'dbt_test__audit',
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'test',
        'severity': 'ERROR',
        'store_failures': None,
        'where': None,
        'limit': None,
        'fail_calc': 'count(*)',
        'warn_if': '!= 0',
        'error_if': '!= 0',
    })
"""


TEST_CONFIG_V1A = """
    config: Optional[TestConfig] = {
        'enabled': True,
        'materialized': 'test',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'severity': 'ERROR',
    }
"""

TEST_CONFIG_V1A_REPLACE = """
    config: Optional[TestConfig] = TestConfig(**{
        'enabled': True,
        'materialized': 'test',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'severity': 'ERROR',
    })
"""



DEPENDS_ON = """
    depends_on: Optional[DependsOn] = {'macros': [], 'nodes': []}
"""

DEPENDS_ON_REPLACE = """
    depends_on: Optional[DependsOn] = DependsOn(**{'macros': [], 'nodes': []})
"""


DOCS = """
    docs: Optional[Docs] = {'show': True}
"""

DOCS_REPLACE = """
    docs: Optional[Docs] = Docs(**{'show': True})
"""


SEED_CONFIG = """
    config: Optional[SeedConfig] = {
        'enabled': True,
        'materialized': 'seed',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'quote_columns': None,
        'post-hook': [],
        'pre-hook': [],
    }
"""

SEED_CONFIG_REPLACE = """
    config: Optional[SeedConfig] = SeedConfig(**{
        'enabled': True,
        'materialized': 'seed',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'quote_columns': None,
        'post-hook': [],
        'pre-hook': [],
    })
"""


SEED_CONFIG_V1 = """
    config: Optional[SeedConfig] = {
        'enabled': True,
        'materialized': 'seed',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'quote_columns': None,
    }
"""

SEED_CONFIG_V1_REPLACE = """
    config: Optional[SeedConfig] = SeedConfig(**{
        'enabled': True,
        'materialized': 'seed',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'quote_columns': None,
    })
"""


SEED_CONFIG_V2 = """
    config: Optional[SeedConfig] = {
        'enabled': True,
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'seed',
        'persist_docs': {},
        'quoting': {},
        'column_types': {},
        'full_refresh': None,
        'on_schema_change': 'ignore',
        'quote_columns': None,
        'post-hook': [],
        'pre-hook': [],
    }
"""

SEED_CONFIG_V2_REPLACE = """
    config: Optional[SeedConfig] = SeedConfig(**{
        'enabled': True,
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'seed',
        'persist_docs': {},
        'quoting': {},
        'column_types': {},
        'full_refresh': None,
        'on_schema_change': 'ignore',
        'quote_columns': None,
        'post-hook': [],
        'pre-hook': [],
    })
"""

NODE_CONFIG = """
    config: Optional[NodeConfig] = {
        'enabled': True,
        'materialized': 'view',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'post-hook': [],
        'pre-hook': [],
    }
"""

NODE_CONFIG_REPLACE = """
    config: Optional[NodeConfig] = NodeConfig(**{
        'enabled': True,
        'materialized': 'view',
        'persist_docs': {},
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
        'post-hook': [],
        'pre-hook': [],
    })
"""

NODE_CONFIG_V1 = """
    config: Optional[NodeConfig] = {
        'enabled': True,
        'materialized': 'view',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
    }
"""

NODE_CONFIG_V1_REPLACE = """
    config: Optional[NodeConfig] = NodeConfig(**{
        'enabled': True,
        'materialized': 'view',
        'persist_docs': {},
        'post-hook': [],
        'pre-hook': [],
        'vars': {},
        'quoting': {},
        'column_types': {},
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'full_refresh': None,
    })
"""


NODE_CONFIG_V2 = """
    config: Optional[NodeConfig] = {
        'enabled': True,
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'view',
        'persist_docs': {},
        'quoting': {},
        'column_types': {},
        'full_refresh': None,
        'on_schema_change': 'ignore',
        'post-hook': [],
        'pre-hook': [],
    }
"""

NODE_CONFIG_V2_REPLACE = """
    config: Optional[NodeConfig] = NodeConfig(**{
        'enabled': True,
        'alias': None,
        'schema': None,
        'database': None,
        'tags': [],
        'meta': {},
        'materialized': 'view',
        'persist_docs': {},
        'quoting': {},
        'column_types': {},
        'full_refresh': None,
        'on_schema_change': 'ignore',
        'post-hook': [],
        'pre-hook': [],
    })
"""


MACRO = """
    depends_on: Optional[MacroDependsOn] = {'macros': []}
"""

MACRO_REPLACE = """
    depends_on: Optional[MacroDependsOn] = MacroDependsOn(**{'macros': []})
"""


EXPOSURE = """
    resource_type: Optional[ResourceType18] = 'exposure'
"""

EXPOSURE_REPLACE = """
    resource_type: Optional[ResourceType18] = ResourceType18.exposure
"""


QUOTING = """
    quoting: Optional[Quoting] = {
        'database': None,
        'schema': None,
        'identifier': None,
        'column': None,
    }
"""

QUOTING_REPLACE = """
    quoting: Optional[Quoting] = Quoting(**{
        'database': None,
        'schema': None,
        'identifier': None,
        'column': None,
    })
"""

SOURCE_CONFIG = """
    config: Optional[SourceConfig] = {'enabled': True}
"""

SOURCE_CONFIG_REPLACE = """
    config: Optional[SourceConfig] = SourceConfig(**{'enabled': True})
"""


DT_IMPORT = """
from datetime import datetime
"""

DT_IMPORT_REPLACE = """
from datetime import datetime
from dateutil import parser
"""

CONSTR1 = """
    severity: Optional[
        constr(regex=r'^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$', strict=True)
    ] = 'ERROR'
"""

CONSTR1_REPLACE = """
    severity: Optional[  # type: ignore
        constr(regex=r'^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$', strict=True)
    ] = 'ERROR'
"""


CONSTR2 = """
    user_id: Optional[
        Optional[
            constr(
                regex=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
                strict=True,
            )
        ]
    ] = Field(None, description='A unique identifier for the user')
"""

CONSTR2_REPLACE = """
    user_id: Optional[  # type: ignore
        Optional[
            constr(
                regex=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
                strict=True,
            )
        ]
    ] = Field(None, description='A unique identifier for the user')
"""


CONSTR3 = """
    user_id: Optional[
        Optional[
            constr(
                regex=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
            )
        ]
    ] = Field(None, description='A unique identifier for the user')
"""

CONSTR3_REPLACE = """
    user_id: Optional[  # type: ignore
        Optional[
            constr(
                regex=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
            )
        ]
    ] = Field(None, description='A unique identifier for the user')
"""

CONSTR4 = """
    severity: Optional[
        constr(regex=r'^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$')
    ] = 'ERROR'
"""

CONSTR4_REPLACE = """
    severity: Optional[  # type: ignore
        constr(regex=r'^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$')
    ] = 'ERROR'
"""


GENAT = """
    generated_at: Optional[datetime]
"""

GENAT_REPLACE = """
    generated_at: Optional[Union[datetime,str]]
"""


GENAT = """
    resource_type: Optional[ResourceType20] = 'exposure'
"""

GENAT_REPLACE = """
    generated_at: Optional[Union[datetime,str]]
"""

EXPOSURE_V4 = """
    resource_type: Optional[ResourceType20] = 'exposure'
"""

EXPOSURE_V4_REPLACE = """
    resource_type: Optional[ResourceType20] = ResourceType20.exposure
"""

METRICS = """
    resource_type: Optional[ResourceType21] = 'metric'
"""

METRICS_REPLACE = """
    resource_type: Optional[ResourceType21] = ResourceType21.metric
"""


TIME = """Optional[Optional[Time]] = {'count': None, 'period': None}"""

TIME_REPLACE = """Optional[Optional[Time]] = Time(**{'count': None, 'period': None})"""


LOOKUP = [
    [TEST_CONFIG, TEST_CONFIG_REPLACE],
    [TEST_CONFIG_V2, TEST_CONFIG_V2_REPLACE],
    [TEST_CONFIG_V1A, TEST_CONFIG_V1A_REPLACE],
    [DEPENDS_ON, DEPENDS_ON_REPLACE],
    [DOCS, DOCS_REPLACE],
    [SEED_CONFIG, SEED_CONFIG_REPLACE],
    [SEED_CONFIG_V1, SEED_CONFIG_V1_REPLACE],
    [SEED_CONFIG_V2, SEED_CONFIG_V2_REPLACE],
    [NODE_CONFIG, NODE_CONFIG_REPLACE],
    [NODE_CONFIG_V1, NODE_CONFIG_V1_REPLACE],
    [NODE_CONFIG_V2, NODE_CONFIG_V2_REPLACE],
    [MACRO, MACRO_REPLACE],
    [EXPOSURE, EXPOSURE_REPLACE],
    [EXPOSURE_V4, EXPOSURE_V4_REPLACE],
    [QUOTING, QUOTING_REPLACE],
    [SOURCE_CONFIG, SOURCE_CONFIG_REPLACE],
    [CONSTR1, CONSTR1_REPLACE],
    [CONSTR2, CONSTR2_REPLACE],
    [CONSTR3, CONSTR3_REPLACE],
    [CONSTR4, CONSTR4_REPLACE],
    [GENAT, GENAT_REPLACE],
    [TIME, TIME_REPLACE],
    [METRICS, METRICS_REPLACE],
]


ISO_DT_REGEX = r'(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?'


def add_datetime(content: str) -> str:
    """
    Function that search for iso format datetime and change str
    to datetime object
    """
    # match_iso8601 = re.compile(ISO_DT_REGEX).match
    new_contents = re.finditer(ISO_DT_REGEX, content)
    datetimes = [n.group(0) for n in new_contents]
    print(f"search for regex in {len(content)}")
    print(datetimes)
    for _ in datetimes:
        content = content.replace(f"'{_}'", f"'{_}'  # type: ignore")
        if _ not in content:
            raise ValueError(f"{_} is not found!")
        else:
            print(f"{_} found!")
    return content


def lookup_replace(file_path):
    """
    Function that looks for a certain regex pattern and replaces it
    to have a valid mypy
    """
    with open(file_path, "r+") as file:
        file_contents = file.read()
        file_contents = add_datetime(file_contents)
        for rep in LOOKUP:
            if rep[0] in file_contents:
                print("Found in file")
                occ = file_contents.count(rep[0])
                # print(f"Found in file: {occ} times")
                file_contents = file_contents.replace(rep[0], rep[1])
            else:
                print('not in file')
        # print(file_contents)
        
        file.seek(0)
        file.truncate()
        file.write(file_contents)


def replace(file_path):
    """
    Function that looks for a certain regex pattern and replaces it
    to have a valid mypy
    """
    found_expressions = []
    new_file = ''
    with open(file_path, "r+") as file:
        file_contents = file.read()
        # new_contents = re.sub(r "(\b\d+\.\d+)[a-z]", r "\1 seconds", file_contents) #substitutes 8.13 s
        new_contents = re.findall(r'Optional(.*?){', file_contents)
        # print(new_contents)
        for matchword in new_contents:
            if not 'Dict' in matchword:
                object_name = re.match(r'\[(.*?)\]', matchword)
                start = object_name.pos
                raw = object_name.group(0)[start+1:-1]
                x = {"key_name": raw, "match": object_name.group(0), "matchword": matchword}
                found_expressions.append(x)
        # find and replace
        for entry in found_expressions:
            print(entry)
            raw = entry["key_name"]
            matchword = entry["matchword"]
            # found = re.findall(re.escape(matchword), file_contents)
            # print(found)
            if raw == "DependsOn":
                replace_with = f"{matchword}{raw}(**"
                replace_end_with = "}"
                print(replace_with)
                m = re.findall(re.escape(matchword), file_contents)
                print(len(m))
                generate = re.sub(re.escape(matchword), replace_with, file_contents)
                new_file += generate
        
        file.seek(0)
        file.truncate()
        file.write(generate)


if __name__ == "__main__":
    files = ['v1.py', 'v2.py', 'v3.py', 'v4.py', ]
    base_path = os.path.join(os.path.dirname( __file__ ), '..', 'dagserializer', 'dbtschematas')
    for f in files:
        target_file = os.path.join(base_path, f)
        lookup_replace(target_file)


