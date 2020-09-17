import csv
import numpy as np

with open("data/house.csv") as f:
    loyers = []
    surfaces = []
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
nployers = np.array(loyers)
npsurfaces = np.array(surfaces)

print(nployers)
print(np.max(nployers / npsurfaces))
