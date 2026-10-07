import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt
from numpy.random import weibull

df = pd.read_csv("data/house/house.csv")
print(df)
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
df.to_excel("data/house/house.xlsx", index=False)
print(np.mean(df["loyer_m2"]) ,np.std(df["loyer_m2"]))



df = df[(df["surface"] < 200) & (df["loyer"] < 20000)]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df["surface"], df["loyer"])
print(slope, intercept, rvalue, pvalue, stderr)

x = np.arange(200)
y = slope * x + intercept

def poly2(x, a, b ,c):
    return a * x ** 2 + b * x + c

weight, cov = opt.curve_fit(poly2, df["surface"], df["loyer"])
print(weight)


plt.scatter(df["surface"], df["loyer"])
plt.plot(x, y, color="red")
plt.plot(x, poly2(x, weight[0], weight[1], weight[2]), color="black")
plt.show()
