import numpy as np

dico = np.load("data/house/house.npz")
print(dico["loyers"], dico["surfaces"])

# Afficher pour loyers, le max, le min, sum/len
# Créer le vecteur loyer_m2 = loyers/surfaces
# Filtrer les surfaces < 200
# Bonus : Filtrer les loyers dont la surface < 200