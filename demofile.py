import csv
import pickle

with open("data/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    loyers_per_m2 = []
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        print(loyer / surface)
        loyers.append(loyer)
        surfaces.append(surface)
        loyers_per_m2.append(loyer / surface)
    print(loyers)
    print(surfaces)
    print(min(loyers), max(loyers), sum(loyers) / len(loyers))
    with open("data/house.pickle", "wb") as f:
        pickle.dump((loyers, surfaces, loyers_per_m2), f)
with open("data/house.pickle", "rb") as f:
    loyers, surfaces, loyers_per_m2 = pickle.load(f)
    print(loyers)

