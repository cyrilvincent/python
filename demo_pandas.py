import pandas as pd
import matplotlib.pyplot as plt

# dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx") # pip install xlrd
dataframe["loyers_per_m2"] = dataframe.loyer / dataframe["surface"]
print(dataframe.describe())
dataframe.to_html("data/house/house.html")
dataframe_filtered = dataframe[dataframe.surface < 200]
plt.scatter(dataframe_filtered["surface"], dataframe_filtered.loyer)
plt.show()
dataframe_filtered.hist(bins=20)
plt.show()


