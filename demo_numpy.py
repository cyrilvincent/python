import numpy as np

v1 = np.array([1,2,3,4], dtype=np.int32)
v2 = np.array([5,6,7,255])
v2 = v2.astype(np.uint8)
print(v2 + 1)
print(v1.dtype)
print(v1 + 2)
print(v1 * v2)
print(np.sin(v1))
print(np.arange(0,10,2))
print(np.linspace(-2 * np.pi,10,8))

rnd1 = np.random.rand(10)
print(rnd1 * 10)
rnd2 = np.random.randint(0,100,10)
print(rnd2)

print(np.max(v1))

print(v1.dtype, v1.ndim, v1.size, v1.shape)

v100 = np.arange(100) * 2
print(v100)
print(v100[33:-33:2])



