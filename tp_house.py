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

# Afficher le nuage de points x = surfaces et y = loyers

print(np.min(loyers), np.max(loyers), np.mean(loyers), np.std(loyers), np.median(loyers))
loyer_m2 = loyers / surfaces
print(np.mean(loyer_m2), np.median(loyer_m2))
print(surfaces[surfaces > 200])
print(loyers[surfaces > 200])
