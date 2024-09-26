import pandas as pd
import numpy as np

#dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx")

print(dataframe["loyer"], dataframe.surface)

dataframe["loyers_per_m2"] = dataframe["loyer"] / dataframe.surface
print(dataframe)
print(dataframe.describe())

dataframe.to_html("data/house.house.html")

dataframe_filtered = dataframe[dataframe.surface < 200]