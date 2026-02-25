import numpy as np
import matplotlib.pyplot as plt

print(np.__version__)

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

a1 = np.array([1,2,3,4], dtype=np.int64)
a2 = np.array([0.1,0.99], dtype=np.float64)
print(a2.astype(np.uint8))
print(a1)
a3 = np.arange(-np.pi, np.pi, 0.01)
a4 = np.linspace(0,1,11)
rnd = np.random.rand(10)
print(rnd * 10)
rnd2 = np.random.randint(0,100,10)
print(rnd2)

print(a1 ** 2)
print(np.sin(a1))
print(np.sum(a1))
result = a1 ** 2
print(a1)
print(a1.dtype, a1.ndim, a1.size, a1.shape)

for v in a1:
    print(v)

for i in range(a1.size):
    print(a1[i])

print(a1[a1 % 2 == 0])
print(a3[np.sin(a3) > 0])

np.savez("myfile.npz", rnd=rnd)
dico = np.load("myfile.npz")
print(dico["rnd"])

dico = np.load("data/house/house.npz")
print(dico["loyers"])



