# dagserializer



# Get new schema versions from dbt
datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v1.json --output dagserializer/dbtschematas/v1.py


datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v4.json --output dagserializer/dbtschematas/v4.py --strict-types {str,bytes,int,float,bool}


datamodel-codegen --url https://schemas.getdbt.com/dbt/manifest/v4.json --output dagserializer/dbtschematas/v4.py --strip-default-none