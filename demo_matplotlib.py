import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2* np.pi, 100)
y = np.sin(x)
ycos = np.cos(x)

xbar = np.arange(5)
ybar = xbar * 2

plt.subplot(2,2,1)
plt.title("exemple")
plt.scatter(x, y, label="sin")
plt.plot(x, ycos, color="red", label="cos")
plt.legend()
plt.subplot(2,2,4)
plt.bar(xbar, ybar)
plt.savefig("exemple.png")
plt.show()