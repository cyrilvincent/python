import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

x = np.arange(10)
y = np.arange(10)

plt.scatter(x, y, color="green")
plt.plot(x, y)
plt.bar(x,y, color="red")
plt.show()

def f(x):
    return np.sin(x) + np.tanh(x)

g = lambda x: np.sin(x) * np.tanh(x)

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.plot(x, f(x), color="red")
plt.plot(x, g(x), color="green")
plt.show()

plt.subplot(221)
plt.plot(x, f(x), color="red")
plt.subplot(222)
plt.plot(x, g(x), color="green")
plt.show()