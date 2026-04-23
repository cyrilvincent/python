# Afficher 4 suplots
# Sin en scatter
# Cos en plot
# tanh en plot
# la fonction sigmoid https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques)

# Dans le zip téléchargé lundi matin copier le répertoire data à la racine de votre projet
# Vérifier que le répertoire data apparait dans pycharm
# Dans data/house/house.csv

import numpy as np
data = np.load("data/house/house.npz")
loyers = data["loyers"]
surfaces = data["surfaces"]

# Afficher min, max, mean des loyers & surfaces
# Créer le tableau loyer_m2 qui est le loyer par m²
# Afficher dans un scatter x = surfaces, y = loyers
# Bonus : En déduire un modèle mathématique
