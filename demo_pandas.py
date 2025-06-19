import pandas as pd

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
dataframe["loyers_m2"] = dataframe["loyer"] / dataframe.surface
print(dataframe.loyers_m2[dataframe.surface > 100])
print(dataframe)
dataframe.to_excel("data/house/house.xlsx", index=False)
print(dataframe.describe())
