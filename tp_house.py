import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers.shape, surfaces.shape)
print(loyers)

# Afficher min, max, sum(loyers) / len(loyers) pour loyers & surfaces
# loyers_m2, puis afficher min, max, moy
# Créer la fonction qui modélise cela : f(surface) = loyer_m2_moyen * surface

print(np.min(loyers), np.max(loyers))
loyers_m2 = loyers / surfaces
print(np.min(loyers_m2), np.max(loyers_m2), np.sum(loyers_m2) / len(loyers_m2))

def model_loyer(surfaces):
    return surfaces * 37.66

x = np.arange(400)
y = model_loyer(x)
plt.scatter(surfaces, loyers)
plt.plot(x, y, color="red")
plt.show()



if __name__ == '__main__':
    print(model_loyer(100))

# Afficher le nuage de points surfaces / loyers
# Afficher le model_loyer