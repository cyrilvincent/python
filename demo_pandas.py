import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

df = pd.read_csv("data/house/house.csv")

df["loyer_m2"] = df["loyer"] / df["surface"]
df.to_excel("data/house/house.xlsx", index=False)

print(df[df["surface"] > 200])

print(np.mean(df["loyer_m2"]), np.std(df["loyer_m2"]))
print(df.describe())

print(os.getcwd())

plt.scatter(df["surface"], df["loyer"])
plt.show()

