import scipy.stats as stats
import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/house.csv")
x = dataframe.surface[dataframe.surface < 175]
y = dataframe.loyer[dataframe.surface < 175]
plt.scatter(x, y)
slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
print(slope, intercept, rvalue, pvalue, stderr )
f = lambda x: slope * x + intercept
xt = np.arange(0, 175)
plt.plot(xt, f(xt), color="red")
plt.show()
# f(x) = 30x + 288