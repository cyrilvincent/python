# Analyser heart/data_cleaned_up.csv
# ok dataframe pour num == 0
# ko dataframe pour num == 1
# afficher describe pour le dataframe, ok et ko
# L'age, le genre, le chol la pression (thalach) ont ils un lien avec le diagnostique

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

dataframe = pd.read_csv("data/heart/data_cleaned_up.csv")
print(dataframe.describe())
ok = dataframe[dataframe["num"] == 0]
ko = dataframe[dataframe["num"] == 1]
print(ok.describe())
print(ko.describe())
print(dataframe.corr())
