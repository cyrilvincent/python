import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
plt.scatter(dataframe.surface, dataframe.loyer)
slope, intercept, rvalue, pvalue, loss = stats.linregress(dataframe.surface, dataframe.loyer)

x = np.arange(200)
y = slope * x + intercept
plt.plot(x, y, color="red")
dataframe.to_excel("data/house/house.xlsx")
plt.show()
