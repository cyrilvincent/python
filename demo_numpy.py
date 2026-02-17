import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4], dtype=np.int8)
print(a1)
print(a1.dtype)

a2 = np.arange(2,10,3)
print(a2)

a3 = np.linspace(0,1,5)
print(a3)

rnd = np.random.rand(10)
print(rnd)

rnd2 = np.random.randint(0,100,10)
print(rnd2)

a4 = np.arange(4)
print(a1)
print(a4)
print(a1 + a4)
print(a1 * a4)
print(np.sin(a1) * 10 + a4)
print(np.min(a1))

print(a1.dtype, a1.ndim, a1.size, a1.shape)

print(rnd2)
print(rnd2[rnd2 > 50])

np.savez("np.npz", rnd2 = rnd2)
rnd2 = np.load("np.npz")
