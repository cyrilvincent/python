import numpy as np

res = np.load("data/house/house.npz")
print(res)
loyers = res["loyers"]
surfaces = res["surfaces"]
print(loyers.ndim, loyers.size, loyers.shape, loyers.dtype)
# Afficher la même chose pour surfaces
# Afficher le loyer min, max et idem pour surface
# Créer le vecteur loyer_per_m2 = qui représente le loyer par m2
# Afficher min et max
# Afficher le loyer_per_m2 augmenté de 10%
# Afficher les surfaces > 200m2
# Afficher les loyers dont les surfaces > 200m2