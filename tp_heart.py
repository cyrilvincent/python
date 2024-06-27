import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/heart/data_with_nan.csv", na_values=".")
print(dataframe.head())
print(dataframe.describe().T)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num != 0]

print(ok.describe().T)
print(ko.describe().T)

print(dataframe.corr())

dataframe["chol"].hist(bins=20)
plt.show()

# Virer les colonnes slope, ca, thal (drop(["col1"], axis=1))
# Virer les lignes avec des nan => dropna
# Sauvegarder le dataframe nettoyé
# moy = np.mean, std = np.std
# Bonus remplacer les chol manquants par moy +- std * rnd

dataframe = dataframe.drop(["slope", "ca", "thal"], axis=1).dropna()
# dataframe = dataframe.dropna()
dataframe.to_csv("data/heart/dataclean.csv")
mean = np.mean(dataframe.chol)
std = np.std(dataframe.chol)
value = (mean + ((np.random.rand(dataframe.chol.isna.sum()) - 0.5) * 2 * std))
dataframe = dataframe.chol.fillna(value=value, inplace=True)



