from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        fike_data = csv.DictReader(file)
        return [row for row in fike_data]
