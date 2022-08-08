from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        file_data = csv.DictReader(file)
        print(file_data)
        return [row for row in file_data]
