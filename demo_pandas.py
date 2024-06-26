import pandas as pd
import matplotlib.pyplot as plt

serie = pd.Series([1,2,3,4])
print(serie)
serie = serie.drop(2)
print(serie)

dico = {"A":1, "B":2}
print(dico["A"])
dico["A"]=3
dico["C"]=4
print(dico)

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
print(dataframe.surface)
loyer_per_m2 = dataframe.loyer / dataframe.surface
print(loyer_per_m2)
dataframe["loyer_per_m2"] = loyer_per_m2
print(dataframe)
dataframe.to_excel("data/house/house.xlsx") # pip install openpyxl

print(dataframe.describe())

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()