import numpy as np

m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m1)
print(m1.size, m1.ndim, m1.shape)
print(np.sin(m1 * 2))
m2 = np.random.rand(3,3)
print(m1 + m2)
print(m1[:,1:])

v1 = np.arange(12)
print(v1.shape)
m1 = v1.reshape(2,3,2)
print(m1)
print(m1.shape)