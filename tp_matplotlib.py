# Afficher 4 suplots
# Sin en scatter
# Cos en plot
# tanh en plot
# la fonction sigmoid https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques)
import matplotlib.pyplot as plt
# Dans le zip téléchargé lundi matin copier le répertoire data à la racine de votre projet
# Vérifier que le répertoire data apparait dans pycharm
# Dans data/house/house.csv

import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.tanh(x)
y4 = 1 / (1 + np.exp(-x))

plt.subplot(2,2,1)
plt.plot(x, y)
plt.subplot(2,2,2)
plt.scatter(x, y2)
plt.subplot(2,2,3)
plt.plot(x, y3)
plt.subplot(2,2,4)
plt.plot(x, y4)

plt.show()


data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(np.min(loyers), np.max(loyers), np.mean(loyers))
print(np.min(surfaces), np.max(surfaces), np.mean(surfaces))
loyers_m2 = loyers / surfaces
print(np.min(loyers_m2), np.max(loyers_m2), np.mean(loyers_m2))
np.savez("data/house/house2.npz", loyers_m2=loyers_m2, loyers=loyers, surfaces=surfaces)

plt.scatter(surfaces, loyers)
plt.show()



# Afficher min, max, mean des loyers & surfaces
# Créer le tableau loyer_m2 qui est le loyer par m²
# Afficher dans un scatter x = surfaces, y = loyers
# Bonus : En déduire un modèle mathématique
