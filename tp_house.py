import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers)

# min, max, mean, len surfaces & loyers
# loyer_per_m2 + min, max, mean
# surfaces_sup_200 + len

print(np.min(loyers), np.max(loyers), np.mean(loyers), len(loyers))
print(np.min(surfaces), np.max(surfaces), np.mean(surfaces), len(surfaces))

loyer_per_m2 = loyers / surfaces
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2), len(loyer_per_m2))

