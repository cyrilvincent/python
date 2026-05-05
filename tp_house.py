import numpy as np
import matplotlib.pyplot as plt

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

plt.subplot(2,1,1)
plt.scatter(surfaces, loyers)
plt.subplot(2,1,2)
plt.scatter(surfaces[surfaces < 175], loyers[surfaces < 175])

plt.show()