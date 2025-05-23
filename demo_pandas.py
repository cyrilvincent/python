import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/house/house.csv")
loyer_m2 = data["loyer"] / data["surface"]
avg = np.mean(loyer_m2)

x = np.arange(400)
y = avg * x
plt.scatter(data["surface"], data["loyer"])
plt.plot(x, y, color="red")
plt.show()