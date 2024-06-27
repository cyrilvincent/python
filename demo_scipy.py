# pip install scipy
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
slope, intercept, rvalue, pvalue, mse = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue)
print(f"Slope: {slope:.1f}, intercept: {intercept:.1f}, rvalue: {rvalue:.1f}")

x = np.arange(200)
y = slope * x + intercept

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(x, y, color="red")
plt.show()

