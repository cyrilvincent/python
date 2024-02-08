import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.arange(4)

print(v1)
print(v2)
print(v1 + v2)
print(np.sin(v1) * 2)

print(v1 * v2)
print(np.dot(v1, v2))

print(v1.shape)

print(np.mean(v1), np.std(v1), np.var(v1), np.median(v1))

print(1j ** 2 )
a = 1j
b = 2-3j
print(a + b)
j = 2-3j