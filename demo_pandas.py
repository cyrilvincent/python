import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
print(dataframe.describe())

dataframe=dataframe[dataframe.surface < 200]

dataframe["loyer_m2"] = dataframe.loyer / dataframe.surface

dataframe.to_excel("data/house/house.xlsx", index=False)

plt.scatter(dataframe["surface"], dataframe.loyer)
plt.show()

