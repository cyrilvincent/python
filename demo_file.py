# f = open("data/house/house.csv")
# content = f.read()
# print(content)

import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(float(row["loyer"]) / float(row["surface"]))

# Faire la fonction load(path: str) tuple[list[float], list[float]]
# Faire la fonction compute_loyer_per_m2(loyers: list[float], surfaces: list[float) -> list[foat]
# afficher le résultat
