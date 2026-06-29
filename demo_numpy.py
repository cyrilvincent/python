import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4,5])
a2 = np.arange(5)
print(a1, a2)

a3 = a1 + a2
print(a1 * a2)
print(np.cos(a1))
print(a1[np.cos(a1) > 0])

m22 = np.array([[1,2],[3,4]])
print(m22)

v12 = np.arange(12)
print(v12, v12.shape)

m34 = v12.reshape(3, 4)
print(m34, m34.shape)
print(np.cos(m34))
