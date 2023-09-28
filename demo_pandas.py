import pandas as pd

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())
loyers = dataframe.loyer
surfaces = dataframe.surface
print(list(loyers))
print(list(surfaces))

