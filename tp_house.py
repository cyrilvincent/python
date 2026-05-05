import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]

# Afficher loyer min, max
# Idem pour surface
# Créer le tableau loyer_m2
# Filtrer les surfaces > 200
# Filtrer les loyers dont la surface > 200

print(np.min(loyers), np.max(loyers), np.min(surfaces), np.max(surfaces))
loyer_m2 = loyers / surfaces
filter = surfaces > 200
print(surfaces[filter])
print(loyers[filter])