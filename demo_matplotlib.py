import matplotlib.pyplot as plt
import numpy as np

xbar = np.arange(5)
ybar = xbar * 2
#
# plt.bar(x, y)
# plt.show()
#
# plt.bar(x, y, color="red")
# plt.show()

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)
plt.subplot(2,2,1)
plt.title("Trigo")
plt.scatter(x, y, label="sin")
plt.subplot(2,2,4)
plt.plot(x, y2, color="red", label="cos")
plt.legend()
plt.subplot(2,2,2)
plt.bar(xbar, ybar, color="red")
plt.savefig("trigo.svg")
plt.show()