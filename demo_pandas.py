import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Creer la bd access
# Dans panneau de configuration > odbc > Créer une source de données utilisateur
# pip install pyodbc sqlalchemy sqlalchemy-access openpyxl


dataframe = pd.read_csv("data/house/house.csv", )
print(dataframe.dtypes)
dataframe["loyer_m2"] = dataframe["loyer"]/dataframe["surface"]
print(dataframe)
print(dataframe.describe())

# dataframe.to_excel("data/house/house.xlsx")
# dataframe.to_sql("house", r"access+pyodbc://@house" )

plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.show()

# Filter les data pour les surfaces < 100m²

print(np.mean(dataframe["loyer"]), np.std(dataframe["loyer"]), np.median(dataframe["loyer"]), np.quantile(dataframe["loyer"], [0.1,0.25,0.5,0.75,0.9]))



