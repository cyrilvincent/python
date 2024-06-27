import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/climate/jena_filtered.csv", index_col="Date Time")
temp = dataframe["T (degC)"]
fft = np.fft.fft(temp)
f_dataset = np.arange(len(fft))
years = len(fft) / (24*365.2524)
f_per_year = f_dataset/years
plt.subplot(211)
plt.plot(dataframe.index, temp)
plt.xticks([])
plt.subplot(212)
plt.plot(f_per_year[:len(fft)//2], np.abs(fft[:len(fft)//2]))
plt.xscale("log")
plt.show()
