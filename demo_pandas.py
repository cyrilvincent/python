import pandas as pd

print(pd.__version__)

dataframe = pd.read_csv("data/house/house.csv")
dataframe["loyer_per_m2"] = dataframe["loyer"] / dataframe["surface"]
print(dataframe.describe())
dataframe.to_html("data/house/house.html")
dataframe.to_excel("data/house/house.xlsx", index=False) # pip install openpyxl