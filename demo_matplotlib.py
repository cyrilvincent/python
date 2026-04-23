import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,2,1)
plt.plot(x, y, "rs-", color="red", label="sin \u03C0")
plt.subplot(2,2,2)
plt.scatter(x, y2, color="green", label="cos")
plt.title("sin")
plt.legend()
plt.savefig("toto.svg")
plt.show()