import csv
import matplotlib.pyplot as plt
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
    print(np.mean(loyers_per_m2), np.std(loyers_per_m2), np.median(loyers_per_m2))
    np.savez("data/house/house.npz", loyers=loyers, surfaces=surfaces, loyers_per_m2=loyers_per_m2)
    content = np.load("data/house/house.npz")
    print(content.keys())

    loyer_mean = np.mean(loyers)
    loyer_std = np.std(loyers)
    loyers_greater_mean = loyers[loyers > loyer_mean + 3 * loyer_std]
    surfaces_greater_mean = surfaces[loyers > loyer_mean + 3 * loyer_std]
    print(loyers_greater_mean, surfaces_greater_mean)
    print(list(zip(loyers_greater_mean, surfaces_greater_mean)))

    loyers = loyers[surfaces < 180]
    surfaces = surfaces[surfaces < 180]
    plt.scatter(surfaces, loyers)
    plt.show()