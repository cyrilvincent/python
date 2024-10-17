import numpy as np

print(np.__version__)

v1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(v1)
v2 = np.arange(10)
print(v2)
print(v1 + v2)
v3 = v1 + v2
v4 = np.sin(v1)
print(v4)
v5 = np.array([1,2,3])
# print(v1 + v5)

v6 = np.linspace(0,100,1000)
v7 = np.ones(10)
v8 = np.zeros(10)
v9 = np.full(10,99)

v10 = np.array([1,2,3], dtype=np.uint8)

vrnd = np.random.rand(10)
print(vrnd)
vrnd2 = np.random.randint(0,100,10)
print(vrnd2)
print(np.round(vrnd, 2))

# Reduction
print(np.max(v1))

# Forme
print(v1.ndim, v1.size, v1.shape, v1.dtype)

print(v1[::-2])
# for v in v1:
#     print(v)

print(v1 * v2)
print(np.dot(v1, v2))

# Filtrage
filter = v1[np.sin(v1) > 0]
print(np.sin(v1) > 0)
print(filter)

np.savez("data.npz", filter=filter)
res = np.load("data.npz")
print(res)
print(res["filter"])