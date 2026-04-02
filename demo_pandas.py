import pandas as pd
import numpy as np # pip install openpyxl

df = pd.read_csv("data/house/house.csv")

df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
print(np.mean(df["loyer_m2"]))
df.to_excel("data/house/house.xlsx", index=False)

print(df[df["surface"] > 200])

