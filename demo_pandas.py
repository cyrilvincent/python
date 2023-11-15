import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

dataframe = pd.read_csv("data/house/house.csv") #, index_col="id")
print(dataframe)
loyer_per_m2 = dataframe.loyer / dataframe.surface
print(loyer_per_m2)
print(np.max(loyer_per_m2), np.mean(loyer_per_m2), np.std(loyer_per_m2))
dataframe["loyer_per_m2"] = loyer_per_m2
print(dataframe.head())
print(dataframe.describe())

slope, intercept, rvalue, pvalue, loss = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, loss)
f = lambda x: slope * x + intercept

dataframe = dataframe[dataframe.surface < 200]
plt.scatter(dataframe.surface, dataframe.loyer)
x = np.arange(200)
y = f(x)
plt.plot(x,y,color="red")
plt.show()