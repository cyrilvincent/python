import csv
import numpy as np
import matplotlib.pyplot as plt

with open("data/house.csv") as f:
    loyers = []
    surfaces = []
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
nployers = np.array(loyers)
npsurfaces = np.array(surfaces)

loyersperm2 = nployers / npsurfaces
print(np.min(loyersperm2), np.max(loyersperm2),np.mean(loyersperm2),np.std(loyersperm2))

plt.title("Surfaces / Loyers")
plt.xlabel("Surfaces")
plt.ylabel("Loyers")
plt.scatter(npsurfaces, nployers)
plt.show()
