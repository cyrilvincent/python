import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")

loyer_per_m2 = dataframe.loyer / dataframe.surface
dataframe["loyer_per_m"] = loyer_per_m2

print(dataframe.describe())

dataframe.to_html("out.html")

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()

# TP
# charger house.csv (tester house.xlsx) pip install openpyxl
# Créer la colonne loyer_per_m2
# Calculer la moy + std pour chacune des colonnes
# filtrer les surfaces < 200
# Bonus : filtrer loyer_per_m2 < mean + 3 * std

