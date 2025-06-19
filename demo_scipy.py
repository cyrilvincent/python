import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.integrate as integrate

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[(dataframe.surface < 200) & (dataframe.loyer < 15000)]
plt.scatter(dataframe.surface, dataframe.loyer)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, stderr )

f = lambda x: slope * x + intercept
x = np.arange(200)
plt.plot(x, f(x), color="red")
plt.show()

f = lambda x : np.sin(x) - np.tanh(x)

area = integrate.quad(f, 0, 1)
print(area)


