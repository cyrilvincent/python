import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data/house/house.csv")
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df.describe())
df.to_csv("data/house/house.txt", sep="\t", index=False)
df.to_excel("data/house/house.xlsx", index=False)

print(np.mean(df["loyer"]), np.std(df["loyer"]), np.median(df["loyer"]))

print(df.corr())

print(df[df["surface"] < 200])

slope, intercept, rvalue, _, _ = stats.linregress(df["surface"], df["loyer"])
print(rvalue)

plt.scatter(df["surface"], df["loyer"])
x = np.arange(400)
plt.plot(x, slope * x + intercept, color="red")
plt.show()

df.hist(bins=10)
plt.show()
