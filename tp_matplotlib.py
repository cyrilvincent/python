import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house/house.csv")
plt.scatter(df.surface, df.loyer)
plt.show()

