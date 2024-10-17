import pandas as pd
import numpy as np

pd.options.display.max_columns = None
dataframe = pd.read_csv("data/heart/data_cleaned_up.csv")
print(dataframe.describe())

# num == 1 ko
# num == 0 ok

# Créer le dtaframe ok pour les patients ok
# idem pour ko
# Faites les stats et en déduire des conclusions sur le sex, chol, thalach!, age?
