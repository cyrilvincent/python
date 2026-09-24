import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/house/house.npz")
print(data)
surfaces = data["surfaces"]
loyers = data["loyers"]



loyers_m2 = loyers / surfaces

loyer_m2_mean = np.mean(loyers_m2)
loyer_m2_std = np.std(loyers_m2)

loyers_filtered = loyers[loyers_m2 < loyer_m2_mean + 3 * loyer_m2_std]
surfaces_filtered = surfaces[loyers_m2 < loyer_m2_mean + 3 * loyer_m2_std]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtered ,loyers_filtered)
print(slope, intercept, rvalue, pvalue, stderr)

f = lambda x: slope * x + intercept

x = np.arange(400)
y = f(x)
plt.scatter(surfaces_filtered, loyers_filtered)
plt.plot(x, y, color="red")
plt.show()