import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data/house/house.csv")
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df.describe())
df.to_csv("data/house/house.txt", sep="\t", index=False)
df.to_excel("data/house/house.xlsx", index=False)

print(df.corr())

print(df[df["surface"] < 200])

plt.scatter(df["surface"], df["loyer"])
plt.show()

df.hist(bins=10)
plt.show()
