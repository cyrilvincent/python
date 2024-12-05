import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

dataframe = pd.read_csv("data/cancer/data.csv", index_col="id")
# print(dataframe.describe().T)

# OK : diagnosis == 0
# KO : diagnosis == 1
# Describe
# area, perimeter, concavity => mean, std
ok = dataframe[dataframe.diagnosis == 0]
ko = dataframe[dataframe.diagnosis == 1]
print(ok.describe().T)
print(ko.describe().T)

plt.matshow(dataframe.corr())
# plt.yticks(dataframe.columns, rotation=0)
plt.show()
