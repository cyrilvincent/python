import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 180]
loyer = dataframe["loyer"]
surface = dataframe.surface
loyer_per_m2 = loyer / surface
dataframe["loyer_per_m2"] = loyer_per_m2
print(dataframe)
dataframe.to_json("data/house/house.json", indent=4)
dataframe.to_xml("data/house/house.xml",pretty_print=True,root_name="loyers",row_name="loyer")
dataframe.to_excel("data/house/house.xlsx")

slope, intercept, rvalue, _, __ = stats.linregress(surface, loyer)
print(slope, intercept, rvalue)
x = np.arange(180)
y = slope * x + intercept

plt.scatter(surface, loyer)
plt.plot(x, y, color="red")
plt.show()

