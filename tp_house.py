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

print(surfaces.ndim, surfaces.size, surfaces.shape, surfaces.dtype)
print(np.max(surfaces), np.max(loyers))
loyer_per_m2 = loyers / surfaces
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2))
print(loyer_per_m2 * 1.1)
print(surfaces[surfaces > 200])
print(loyers[surfaces > 200])
predicat = surfaces > 200
# print(predicat)
print(surfaces[predicat])
print(loyers[predicat])