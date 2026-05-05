import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/climate/jena_filtered.csv")
y = df["T (degC)"][::24]
x = np.arange(len(y))
plt.plot(x, y)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, df["T (degC)"][::24])
print(slope, intercept)
print(len(x))

plt.plot(x, slope * x + intercept, color="red")

plt.show()
