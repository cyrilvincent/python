import pandas as pd
import numpy as np

dataframe = pd.read_excel("data/E2V.xlsx", sheet_name=0)
print(dataframe.Part6.describe())
part6 = dataframe.Part6 # dataframe["Part6"]
print(np.mean(part6))
puissance = dataframe.Part6 * dataframe.Part7
dataframe["puissance"] = puissance
dataframe.to_csv("data/E2V.csv")
dataframe.to_html("data/E2V.html")

import matplotlib.pyplot as plt
plt.scatter(dataframe["Time (min)"], dataframe.Part45)
# plt.yscale("log")


import scipy.stats as stats
res = stats.linregress(dataframe["Time (min)"], dataframe.Part45)
print(res)
f = lambda x: res[0]*x + res[1]
x = np.arange(8000)
y = f(x)
plt.plot(x, y, color="red")
plt.show()