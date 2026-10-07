import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house/house.csv")
print(df)
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
df.to_excel("data/house/house.xlsx", index=False)

df = df[(df["surface"] < 200) & (df["loyer"] < 20000)]

plt.scatter(df["surface"], df["loyer"])
plt.show()
