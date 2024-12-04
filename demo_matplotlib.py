import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * np.sin(x)

def g(x):
    return np.sin(x)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y1 = f(x)
y2 = g(x)


plt.subplot(211)
plt.scatter(x, y1, color="red", label="xsinx")
plt.subplot(212)
plt.plot(x, y2, "g^-", label="sinx")
plt.title("Demo")
plt.xlabel("temps")
plt.ylabel("values")
plt.legend()
plt.savefig("data/out.svg")
plt.show()
