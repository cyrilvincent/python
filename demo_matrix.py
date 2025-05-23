import numpy as np

m22 = np.array([[1,2],[3,4]])
m22_bis = np.array([[5,6],[7,8]])
print(m22)
m23 = np.array([[1,2,3],[4,5,6]])
print(m23)
print(m23.ndim, m23.size, m23.shape) # row first

print(m22 * 2)
print(m22 * np.array([1,2]))
print(m22.T)
print(m22 * m22_bis)
print(np.dot(m22, m22_bis))
print(np.sin(m22))

print(m23)
print(np.sum(m23))
print(np.sum(m23, axis=0))
print(np.sum(m23, axis=1))

v3 = np.array([1,2,3])
m13 = np.array([[1,2,3]])
m31 = np.array([[1],[2],[3]])
print(v3)
print(m13)
print(m31)