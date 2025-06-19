# Afficher le nuage de points surfaces / loyers
# Ajouter title
# Ajouter des label et legend
# Ajouter des couleurs

import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("data/house/house.csv")
plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()