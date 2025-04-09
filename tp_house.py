import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers)

# min, max, mean, len surfaces & loyers
# loyer_per_m2 + min, max, mean
# surfaces_sup_200 + len

