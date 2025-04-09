import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y, color="red", label="sin")
plt.scatter(x, y2, color="green")
plt.legend()
plt.title("DEMO")
plt.savefig("data.png")
plt.show()
plt.bar(x[:10], y[:10])
plt.show()

