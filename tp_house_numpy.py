# Charger house.csv et reconstruire loyers et surfaces (copier coller)
# Transformer loyers et surfaces en tableau numpy
# Calculer loyers_per_m2
# Faire des stats sur loyers_per_m2
import csv
import numpy as np

with open("data/house/house.csv", "r") as f:
    loyers = []
    surfaces = []
    reader = csv.DictReader(f)
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        loyers.append(loyer)
        surfaces.append(surface)

loyers = np.array(loyers)
surfaces = np.array(surfaces)

loyers_per_m2 = loyers / surfaces
print(loyers_per_m2)

print(np.mean(loyers_per_m2), np.std(loyers_per_m2), np.median(loyers_per_m2), np.quantile(loyers_per_m2, [0.25, 0.75]))
