import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house/house.csv")
df = df[df.surface < 200]
print(df.describe())
plt.scatter(df.surface, df.loyer)
plt.show()

