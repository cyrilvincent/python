import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers.shape, surfaces.shape)
print(loyers)

# Afficher min, max, sum(loyers) / len(loyers) pour loyers & surfaces
# loyers_m2, puis afficher min, max, moy
# Créer la fonction qui modélise cela : f(surface) = loyer_m2_moyen * surface