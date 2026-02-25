import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

# plt.plot(x, y, "rs--")
plt.subplot(2,2,1)
plt.plot(x, y, label="sin", color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.legend()
plt.subplot(2,2, 2)
plt.scatter(x, y2, color="red")
plt.savefig("myplot.png")
plt.show()

# TP Afficher un nuage de points surfaces / loyers
# En déduire une modélisation possible