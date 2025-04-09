# Charger avec pandas data/heart/data_cleaned_up
# ok = [num==0]
# ko = [num=1]
# Faire un describe sur ok et ko
# En déduire des choses

import pandas as pd

dataframe = pd.read_csv("data/heart/data_cleaned_up.csv")
pd.set_option('display.max_columns', None)
# ok = dataframe[(dataframe.num == 0) & (dataframe.sex==0)]
ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]

print(ok.describe().T)
print(ko.describe().T)