import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, stderr)

plt.scatter(dataframe.surface, dataframe.loyer)
x = np.arange(400)
y = slope * x + intercept
plt.plot(x, y, color="red")
plt.show()