import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers)

# Afficher pour loyers & surfaces les min, max, mean, meadian, std
# Créer le tableau loyer_m2 qui est le loyer par m²
# Afficher le loyer par m² moyen
# Filtrer les surfaces > 200
# Filtrer les loyers dont la surface > 200
