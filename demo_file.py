# f = open("data/house/house.csv")
# content = f.read()
# print(content)

import csv

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


def compute_loyer_per_m2(loyers: list[float], surfaces: list[float]) -> list[float]:
    loyer_per_m2 = []
    for i in range(len(loyers)):
        loyer_per_m2.append(loyers[i] / surfaces[i])
    return loyer_per_m2

def compute_loyer_per_m2_zip(loyers: list[float], surfaces: list[float]) -> list[float]:
    loyer_per_m2 = []
    for t in zip(loyers, surfaces):
        loyer_per_m2.append(t[0] / t[1])
    return loyer_per_m2

def compute_loyer_per_m2_intention(loyers: list[float], surfaces: list[float]) -> list[float]:
    return [loyer / surface for loyer, surface in zip(loyers, surfaces)]

# Faire la fonction load(path: str) tuple[list[float], list[float]]
# Faire la fonction compute_loyer_per_m2(loyers: list[float], surfaces: list[float) -> list[foat]
# afficher le résultat

loyers, surfaces = load("data/house/house.csv")
res = compute_loyer_per_m2(loyers, surfaces)
res = compute_loyer_per_m2_zip(loyers, surfaces)
res = compute_loyer_per_m2_intention(loyers, surfaces)
print(res)
