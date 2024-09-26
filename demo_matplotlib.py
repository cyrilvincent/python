import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y)
plt.scatter(x, y2)
plt.savefig("data.png")
plt.show()

dataframe = pd.read_csv("data/house/house.csv")
x = dataframe.surface
y = dataframe.loyer


slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
print(slope, intercept, rvalue, pvalue, stderr)

x2 = np.arange(400)
y2 = slope * x2 + intercept

plt.scatter(x, y)
plt.plot(x2, y2, "red")
plt.show()
