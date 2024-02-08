import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.show()



dataframe = pd.read_csv("data/house/house.csv")

res = stats.linregress(dataframe.surface, dataframe.loyer)
x = np.arange(400)
y = res[0] * x + res[1]

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(x, y, "red")
plt.show()