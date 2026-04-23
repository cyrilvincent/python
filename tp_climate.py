# Charger dans un df data/climate/jena_filtered.csv
# min, max mean sur T (degC)
# Afficher en x Date Time et y = T (degC) dans un plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/climate/jena_filtered.csv")

df = df[12::24]
print(df.describe())

df_filtered = df[(df["T (degC)"] <= 0) & (df["rh (%)"] >= 50)]

x = df_filtered["Date Time"]
y = df_filtered["T (degC)"]
plt.plot(x, y)
plt.show()

# Faire une regression lineaire sur T (degC)
# Afficher la regression