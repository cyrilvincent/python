import matplotlib.pyplot as plt
import numpy as np

def xsinx(x):
    return x * np.sin(x)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = xsinx(x)
y2 = np.sin(x)

# Nuage de points = scatter
# Points reliés = plot
# plt.scatter(x, y)
plt.subplot(2,2,1)
plt.plot(x, y, color="red", label="xsinx")
plt.title("xsinx")
plt.subplot(2,2,2)
plt.plot(x, y2, color="green", label="sinx")
plt.savefig("data/plot.png")
plt.subplot(2,2,3)
x = np.arange(5)
y = x
plt.bar(x, y)
plt.legend()
plt.show()


plt.show()


