import pandas as pd
import numpy as np

df = pd.read_csv("data/house/house.csv")

df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
print(np.mean(df["loyer_m2"]))

a1 = np.array([1,2, np.nan, 4])
print(np.nanmean(a1))

df.to_csv("data/house/house2.csv")
df.to_excel("data/house/house.xlsx", index=False)
