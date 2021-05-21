import scipy.optimize as op
import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/house.csv")
x = dataframe.surface[dataframe.surface]
y = dataframe.loyer[dataframe.surface]
plt.scatter(x, y)
f = lambda x, a, b, c, d: a*x**3+b*x**2+c*x+d
weights, conv = op.curve_fit(f, x, y)
print(weights)
xt = np.arange(0, 400)
plt.plot(xt, f(xt, weights[0] , weights[1] , weights[2] , weights[3]), color="red")
plt.show()
