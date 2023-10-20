import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())

plt.scatter(dataframe.surface, dataframe.loyer)
#plt.show()

mat = dataframe.values
print(np.mean(mat, axis=0))
print(np.median(dataframe.loyer))
#np.mean(mat, axis=2)
