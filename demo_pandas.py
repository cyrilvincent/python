import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("data/house/house.csv")

loyer_per_m2 = df.loyer / df.surface
df["loyer_per_m2"] = loyer_per_m2
print(df.describe())
df.to_json("data/house/house.json")

coef, intercept, rvalue, _, __ = stats.linregress(df.surface, df.loyer)
print(coef, intercept, rvalue)

f = lambda x: coef * x + intercept

plt.scatter(df.surface, df.loyer)
plt.plot(df.surface, f(df.surface), "red")
plt.show()

