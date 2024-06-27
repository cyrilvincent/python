import numpy as np

m1 = np.array([[1,2,3],[3,4,3]])
print(m1)
m2 = np.array([[5,6],[7,8]])
# print(m1 + m2)
print(m1.shape, m1.size, m1.ndim)

v1 = np.arange(12)
m34 = v1.reshape(3,4)
print(m34)
m43 = v1.reshape(-1,3)
print(m43)
v1 = m43.reshape(12)
print(v1)
m112 = v1.reshape(1, 12)
print(m112)
m121 = v1.reshape(12, 1)
print(m121)

m1 = np.array([[1,2],[3,4]])
print(np.linalg.inv(m1))

print(m43)
print(m43[1,1], m43[1], m43[:,-1], m43[:2,1:])

print(m1, np.sum(m1))
print(np.sum(m1, axis=1))

cube232 = v1.reshape(2,3,2)
print(cube232)
print(np.sum(cube232, axis=2))