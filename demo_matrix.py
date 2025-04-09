import numpy as np

m22 = np.array([[1,2],[3,4]])
print(m22)
print(m22 * 2)
print(np.cos(m22))

m22_1 = np.array([[5,6],[7,8]])
print(m22_1)
print(m22 + m22_1)
print(m22 * m22_1)
print(np.dot(m22, m22_1))

m23 = np.array([[1,2,3],[4,5,6]])
print(m23)
# print(m23 + m22)
print(m23.ndim, m23.size, m23.shape)
m32 = m23.T
print(m32)

v12 = np.arange(12)
m34 = v12.reshape(3,4)
print(m34)
v12 = m34.reshape(12)

print(np.sum(m34, axis=1))