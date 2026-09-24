import pandas as pd
# pip install openpyxl

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.columns)
dataframe["loyer_m2"] = dataframe["loyer"] / dataframe["surface"]
print(dataframe[dataframe["surface"] > 200])
dataframe.to_excel("data/house/house.xlsx", index=False)