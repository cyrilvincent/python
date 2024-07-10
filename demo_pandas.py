import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

dataframe = pd.read_csv("data/house/house.csv")

loyer_per_m2 = dataframe.loyer / dataframe.surface
dataframe["loyer_per_m2"] = loyer_per_m2

dataframe = dataframe[dataframe.surface < 200]
mean = np.mean(loyer_per_m2)
std = np.std(loyer_per_m2)

dataframe = dataframe[dataframe.loyer_per_m2 < mean + 3 * std]

print(dataframe.describe())

dataframe.to_html("out.html")



slope, intersect, rvalue, pvalue, mse = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intersect, rvalue, pvalue, mse)
f = lambda x: slope * x + intersect

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(dataframe.surface, f(dataframe.surface), color="red")
plt.show()

# TP
# charger house.csv (tester house.xlsx) pip install openpyxl
# Créer la colonne loyer_per_m2
# Calculer la moy + std pour chacune des colonnes
# filtrer les surfaces < 200
# Bonus : filtrer loyer_per_m2 < mean + 3 * std

