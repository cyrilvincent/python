import numpy as np

print(np.__version__)
a1 = np.array([1,2,3,4], dtype=np.float64)
print(a1.dtype)

a2 = np.arange(10)
for i in a2:
    print(i)


rnd = np.random.rand(10)
print(rnd)
rnd = np.random.randint(0,100,10)
print(rnd)

v4 = np.arange(4)
v4bis = np.array([1,2,3,4])
print(v4, v4bis)
print(v4 + v4bis)
print(np.sin(v4))

# v3 = np.array([1,2,3])
# print(v4 + v3)

print(v4 * v4bis)
print(np.dot(v4, v4bis), v4.dot(v4bis))

print(np.sum(v4), v4.sum())

print(v4.size, v4.shape, v4.ndim)

v4_8bits = v4.astype(np.uint8)
print(v4_8bits - 1)

a100 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
np.set_printoptions(precision=2)
asin = np.sin(a100)
print(asin)
filter = asin > 0
print(filter)
result = asin[filter]
asin[asin > 0]
print(result)
