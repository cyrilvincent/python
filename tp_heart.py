# Charger avec pandas data/heart.data_cleaned_up.csv
# Faire un describe : pd.set_option('display.max_columns', None)
# Afficher dans un matplotlib en x age et en y le chol dans un scatter
# Créer ok = pour num==0
# Créer ko = pour num==1
# Afficher ok.Describe() et ko.describe() qu'en déduire
# Sauvegarder ok en xlsx

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("data/heart/data_cleaned_up.csv")

ok = df[df["num"] == 0]
ko = df[df["num"] == 1]

print(ok.describe())
print(ko.describe())

plt.scatter(ok["age"], ok["chol"], color="green")
plt.scatter(ko["age"], ko["chol"], color="red")
plt.show()

