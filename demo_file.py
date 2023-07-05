import csv
from typing import Tuple, List


def parse_house_csv(path: str) -> Tuple[List[float], List[float]]:
    loyers = []
    surfaces = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            loyer = float(row['loyer'])
            surface = float(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
    return loyers, surfaces

if __name__ == '__main__':
    loyers, surfaces = parse_house_csv("data/house/house.csv")
    print(loyers)

