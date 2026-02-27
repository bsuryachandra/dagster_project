from dagster import asset

@asset
def my_first_asset():
    return [1, 2, 3]

@asset
def my_second_asset(my_first_asset):
    return sum(my_first_asset)

@asset
def my_first_asset():
    return [1, 2, 3, 4]