import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())
loyers = dataframe.loyer
surfaces = dataframe.surface
print(list(loyers))
print(list(surfaces))

loyers_per_m2 = loyers / surfaces
print(loyers_per_m2)
print(loyers_per_m2.describe())

print(np.mean(loyers_per_m2))
print(np.sin(loyers_per_m2))

# plt.scatter(surfaces, loyers)
# plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.tanh(x)
y2 = np.sin(x)
plt.plot(x, y)
plt.plot(x, y2, color="red")
y3 = np.fft.fft(y2)
plt.plot(x, np.real(y3), color="green")
plt.show()



