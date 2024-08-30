from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance
from dagster import EnvVar, Definitions

airbyte_instance = AirbyteResource(
        host=EnvVar("AIRBYTE_HOST").get_value(),
        port=EnvVar("AIRBYTE_PORT").get_value(),
        username=EnvVar("AIRBYTE_USERNAME").get_value(),
        password=EnvVar("AIRBYTE_PASSWORD").get_value(),
    )

airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)

defs = Definitions(
    assets=[airbyte_assets]
)
