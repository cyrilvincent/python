import numpy as np

# row first
m1 = np.array([[1,2],[3,4]])
print(m1)
print(np.sin(m1 * 2))
m2 = np.random.rand(2,2)
print(m2)
print(m2 + m1)
print(np.dot(m1, m2))
print(m1.shape, m1.ndim, m1.size)

v1 = np.arange(12)
print(v1)
m34 = v1.reshape(3,4)
print(m34)
print(m34.T)
print(v1.reshape(4,3))
print(v1.reshape(2,6))
print(m34.reshape(12))
print(v1.reshape(2,2,3))

m1 = np.array([[1,2],[3,4]])
print(np.linalg.inv(m1))