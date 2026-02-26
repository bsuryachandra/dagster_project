# dagster_poc/definitions.py
from dagster import Definitions
from .assets import my_first_asset, my_second_asset
from .trips import taxi_trips_file, taxi_zones_file

defs = Definitions(assets=[my_first_asset, my_second_asset, taxi_trips_file,taxi_zones_file ])