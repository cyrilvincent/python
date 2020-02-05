import csv
import numpy as np

with open("data/mesures.csv") as f:
    reader = list(csv.DictReader(f))
    vt = np.array([float(row["VT"]) for row in reader])
    vm = np.array([float(row["VM"]) for row in reader])
    t = np.array([float(row["T"]) for row in reader])

res = np.abs(vt - vm)
res = t[res > 1]
print(res)
