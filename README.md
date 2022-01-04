# dagserializer


# mypy
Install all missing types

mypy --install-types



# Get new schema versions from dbt
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v1.json --output dagserializer/dbtschematas/v1.py

datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v1.json --allow-population-by-field-name --output dagserializer/dbtschematas/v1_1.py


datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v4.json --output dagserializer/dbtschematas/v4.py --strict-types {str,bytes,int,float,bool}


datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v4.json --output dagserializer/dbtschematas/v4.py --strip-default-none


datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v1.json --allow-population-by-field-name --output dagserializer/dbtschematas/v1.py
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v2.json --allow-population-by-field-name --output dagserializer/dbtschematas/v2.py
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v3.json --allow-population-by-field-name --output dagserializer/dbtschematas/v3.py
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v4.json --allow-population-by-field-name --output dagserializer/dbtschematas/v4.py


# Usefull flags
--use-schema-description
--custom-template-dir dagserializer/codgen_template

# Fixing missing ype extensions
pip install typing-extensions --upgrade

# Running with custom template dir
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v1.json --custom-template-dir /workspace/dagserializer/codgen_template --use-schema-description --output dagserializer/dbtschematas/v1_1.py



### Strategies mypy
1. Set default to None
