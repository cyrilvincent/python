import numpy as np
import pandas as pd
import scipy.optimize as opt
import matplotlib.pyplot as plt
# pip install openpyxl

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.columns)
dataframe["loyer_m2"] = dataframe["loyer"] / dataframe["surface"]
print(dataframe[dataframe["surface"] > 200])
dataframe.to_excel("data/house/house.xlsx", index=False)

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

x = np.arange(400)

weight, cov = opt.curve_fit(poly2, dataframe["surface"], dataframe["loyer"])
print(cov)
plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.plot(x, poly2(x, weight[0], weight[1], weight[2]), color="red")
plt.show()
