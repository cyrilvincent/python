# Importer data/heart/data_cleaned_up.csv
# ok = dataframe pour num = 0
# ko = dataframe pour num = 1
# Afficher la moyenne des ages pour ok et ko

import pandas as pd
import numpy as np
import scipy.stats as stats

dataframe = pd.read_csv("data/heart/data_cleaned_up.csv")
ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(ok.describe())
print(ko.describe())

print(np.abs(dataframe.corr()))