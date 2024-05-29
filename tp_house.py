import csv

import numpy as np


def load(path: str) -> tuple[list[float], list[float]]:
    loyers = []
    surfaces = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            loyer = float(row["loyer"])
            surface = float(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
    return loyers, surfaces

if __name__ == '__main__':
    loyers, surfaces = load("data/house/house.csv")
    loyers = np.array(loyers)
    surfaces = np.array(surfaces)
    print(loyers.size, loyers.ndim, loyers.shape, loyers.dtype)
    print(np.mean(loyers), np.std(loyers), np.median(loyers))
    print(np.mean(surfaces), np.std(surfaces), np.median(surfaces))
    loyers_per_m2 = loyers / surfaces
    print(loyers_per_m2)