# Reprendre demo_scipy
# Faire une regression sur un poly2

import pandas as pd
import matplotlib.pyplot as plt
import datetime
# pip install openpyxl
import scipy.stats as stats
import scipy.optimize as opt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv("data/house/house.csv")

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df["surface"], df["loyer"])
print(slope, intercept, rvalue, pvalue, stderr)

y = slope * df["surface"] + intercept

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weights, conv = opt.curve_fit(poly2, df["surface"], df["loyer"])

xsurf = np.arange(400)
ysurf = poly2(xsurf, weights[0], weights[1], weights[2])

plt.scatter(df["surface"], df["loyer"])
plt.plot(df["surface"], y, color="red")
plt.plot(xsurf, ysurf, color="maroon")
plt.show()
