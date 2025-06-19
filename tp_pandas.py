# Charger data/cancer/data.csv via pandas
# Créer 2 dataframe ok pour diagnosis == 0 et ko pour diagnosis == 1
# Faire des stats
# Sauvegarder les 2 dataframes en Excel et HTML

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
dataframe = pd.read_csv("data/cancer/data.csv")
ok = dataframe[dataframe.diagnosis == 0]
ko = dataframe[dataframe.diagnosis == 1]
print(ok.radius_worst.describe())
print(ko.radius_worst.describe())
plt.matshow(np.abs(dataframe.corr()))
plt.show()
