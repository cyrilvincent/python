import scipy.stats as stats
import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/house.csv")
dataframe = dataframe[dataframe.surface < 200]
tuple = stats.linregress(dataframe.surface, dataframe.loyer)
print(tuple)

plt.scatter(dataframe.surface, dataframe.loyer)
f = lambda x : tuple[0] * x + tuple[1]
x = np.arange(200)
plt.plot(x, f(x))
plt.show()
