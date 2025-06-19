import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)
plt.scatter(x, y)
plt.plot(x, y2, color="red")
plt.show()
