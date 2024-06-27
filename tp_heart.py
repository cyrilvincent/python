import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heart/data_with_nan.csv", na_values=".")
print(dataframe.head())
print(dataframe.describe().T)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num != 0]

print(ok.describe().T)
print(ko.describe().T)

print(dataframe.corr())

dataframe.chol.hist(bins=20)
plt.show()

# Virer les colonnes slope, ca, thal (drop(["col1"], axis=1))
# Virer dropna
# Sauvegarder le dataframe nettoyé
# moy = np.mean, std = np.std
# Bonus remplacer les chol manquants par moy +- std * rnd
