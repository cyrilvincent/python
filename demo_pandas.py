import pandas as pd
import matplotlib.pyplot as plt
# pip install pyodbc sqlalchemy sqlalchemy-access

dataframe = pd.read_csv("data/house/house.csv", )
print(dataframe.dtypes)
dataframe["loyer_m2"] = dataframe["loyer"]/dataframe["surface"]
print(dataframe)
print(dataframe.describe())

dataframe.to_excel("data/house/house.xlsx")
dataframe.to_sql("house", r"access+pyodbc://@house")

plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.show()

# Filter les data pour les surfaces < 100m²



