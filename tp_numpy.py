import numpy as np

data = np.load("data/house/house.npz")
print(data)
surfaces = data["surfaces"]
loyers = data["loyers"]

# Créer le vecteur loyer_m2
# afficher les min et max des surfaces et loyers
# Afficher les surfaces > 200
# Afficher les loyers dont la surface > 200

loyer_m2 = surfaces / loyers
print(np.min(surfaces), surfaces.max())
filter = surfaces > 200
print(surfaces[filter])
print(loyers[filter])

# Afficher le scatter surfaces vs loyers