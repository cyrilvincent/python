import pandas as pd
import numpy as np # pip install openpyxl

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/heart/data_cleaned_up.csv")
print(df)
print(df.corr())

# OK = num==0 df[df["num"]==0]
# KO = num == 1
# np.mean + np.std pour age + sex + chol + thalach

