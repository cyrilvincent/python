import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.arange(4)
print(a2)

a3 = np.arange(0,10, dtype=np.float64)
print(a3)
a4 = np.linspace(0,9,10)
print(a4)

np.random.seed(42)
rnd = np.random.rand(10)
print(rnd)
rnd2 = np.random.randint(0,100,10)
print(rnd2)

print(a1)
result = np.sin(a1) + a2
print(result)
print(a1)

# a5 = np.arange(5)
# print(a1 + a5)
print(np.sum(a1))

bytes = np.arange(252, 256, dtype=np.uint8)
print(bytes + 1)
print(a1.dtype, a1.ndim, a1.size, a1.shape)

print(a1[a1 % 2 == 0])
result = a1 * 2
np.savez("myfile.npz", result=result)

data = np.load("myfile.npz")
print(data)
result = data["result"]
print(result)
result = None
