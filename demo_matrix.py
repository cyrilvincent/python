import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)

m23 = np.array([[1,2,3],[4,5,6]])
print(m23)
print(m23.ndim, m23.size, m23.shape)

m32 = np.array([[1,2],[3,4],[5,6]])
print(m32)
print(np.sin(m32) ** 2)
# print(m23 + m32)

v12 = np.arange(12)
print(v12)
m34 = v12.reshape(-1, 4)
print(m34)

print(m23)
print(np.sum(m23, axis=0))
print(np.sum(m23, axis=1))
