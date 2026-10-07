import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("data/climate/jena_filtered.csv")
temp = df["T (degC)"]
temp = temp[11::24]
x = np.arange(len(temp))

result = np.fft.fft(temp)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, temp)
print(slope * 365)


plt.title("Température Jena")
plt.subplot(2,1,1)
plt.plot(x, temp)
plt.plot(x, slope * x + intercept, color="red")
plt.subplot(2,1,2)
plt.plot(x, np.abs(result))
plt.xscale("log")
plt.show()