import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)
plt.title("sin & cos")
plt.subplot(2,2,1)
plt.plot(x, y, label="sin")
plt.plot(x,y)
plt.legend()
plt.subplot(2,2,2)
plt.plot(x, y2, color="red", label="cos")
plt.legend()
plt.subplot(2,2,3)
plt.bar(np.array([1,2,3,4]), np.array([2,3,1,-2]))
plt.savefig("plt.png")
plt.show()
