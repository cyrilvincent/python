import pandas as pd
import numpy as np
# pip install openpyxl

dataframe = pd.read_csv("data/house/house.csv", delimiter=",", decimal=".")
dataframe["loyer_m2"] = dataframe["loyer"] / dataframe["surface"]
dataframe["sin"] = np.sin(dataframe["loyer_m2"] )
dataframe["mask"] = dataframe["surface"] < 50
print(dataframe)
dataframe.to_csv("data/house/house2.csv", index=False)
dataframe.to_excel("data/house/house.xlsx")
dataframe.to_html("data/house/house.html")
dataframe.to_json("data/house/house.json", indent=2, index=False)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(dataframe.describe())

