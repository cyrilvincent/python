import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/house/house.csv")
df = df[df.surface < 200]
plt.scatter(df.surface, df.loyer)

slope, intercept, rvalue, pvalue, stderr = scipy.stats.linregress(df.surface, df.loyer)
x = np.arange(200)
y = slope * x + intercept
plt.plot(x, y, color="red")
print(slope, intercept, rvalue, pvalue, stderr)
plt.show()