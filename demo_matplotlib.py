import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,2,1)
plt.plot(x, y, color="red", label="sin")
plt.subplot(2,2,2)
plt.scatter(x, y2)
plt.title("sin & cos")
plt.legend()
plt.show()
