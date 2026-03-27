import numpy
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,2,3,4])
print(v1)

# x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
# print(x)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
print(x)

rnd = np.random.rand(10)
print(rnd)
rnd = np.random.randint(0,100,10)
print(rnd)

print(v1 ** 2)
print(np.sin(x))

v2 = np.array([5,6,7,8])
print(v1 + v2)

print(np.mean(v2), np.std(v2))

plt.subplot(2,2,1)
plt.plot(x, np.sin(x), color="red")
plt.plot(x, np.cos(x), color="green")
plt.title("sin+cos")

plt.subplot(2,2,4)
plt.bar([1,2,3,4],[1,2,3,4])

plt.show()

