import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/house/house.npz")

loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers)

# min, max, mean, len surfaces & loyers
# loyer_per_m2 + min, max, mean
# surfaces_sup_200 + len

print(np.min(loyers), np.max(loyers), np.mean(loyers), len(loyers))
print(np.min(surfaces), np.max(surfaces), np.mean(surfaces), len(surfaces))

loyer_per_m2 = loyers / surfaces
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2), len(loyer_per_m2))

surfaces_200 = surfaces[surfaces > 200]
print(len(surfaces_200))

mean = np.mean(loyer_per_m2)

x = np.arange(400)
y = mean * x

plt.scatter(surfaces, loyers, label="loyers")
plt.plot(x, y, color="red", label="model")
plt.legend()
plt.title("Surfaces / Loyers")
plt.show()

