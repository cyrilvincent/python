import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(211)
xbar = np.arange(10)
plt.bar(xbar, xbar)
plt.subplot(212)
plt.scatter(x, y, color="green")
plt.plot(x, y2)
plt.savefig("data/house/house.png")
plt.show()


# surfaces ,loyers
# Afficher le nuage de points surfaces / loyers