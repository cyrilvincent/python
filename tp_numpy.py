import numpy as np

data = np.load("data/house/house.npz")
print(data)
surfaces = data["surfaces"]
loyers = data["loyers"]

# Créer le vecteur loyer_m2
# afficher les min et max des surfaces et loyers
# Afficher les surfaces > 200
# Afficher les loyers dont la surface > 200

