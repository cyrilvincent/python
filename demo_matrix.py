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
print(np.linalg.inv(m22))

v12 = np.arange(12)
mat34 = v12.reshape(3,4)
print(mat34)
mat43 = v12.reshape(-1,3)
print(mat43)
v12 = mat43.reshape(-1)
cube232 = v12.reshape(2,3,2)
print(cube232)
print(cube232[1,1,1])
for row in cube232:
    for col in row:
        for val in col:
            print(val)
np.transpose(cube232, (0,1))