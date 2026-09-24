# Charger jena_filtered avec pandas
# Prendre la temperature à midi [11::24]
# Afficher dans un plot
# Une regression lineaire recuperer la slope * 365

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("data/climate/jena_filtered.csv")
col = "T (degC)"
df = df[11::24]
df[col].loc(55)

x = np.arange(len(df))
slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, df[col])
print(slope * 365)

f = lambda x: slope * x + intercept

plt.plot(x, df[col])
plt.plot(x, f(x), color="red")
plt.show()

