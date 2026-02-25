import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(np.sin(mat1 * 2))
for row in mat1:
    for col in row:
        print(col)
mat1[1,1]=33
print(mat1)

mat2 = np.array([[1,2,3],[4,5,6]])
print(mat2.ndim, mat2.size, mat2.shape)
mat13 = np.array([[1,2,3]])
mat31 = np.array([[1],[2],[3]])
v3 = np.array([1,2,3])
print(mat13.shape)
print(mat31.shape)
print(v3)
print(mat2.T)
mat3 = np.array([[5,6],[7,8]])
print(np.dot(mat1, mat3))

v12 = np.arange(12)
print(v12)
m43 = v12.reshape(-1,3)
print(m43)
m26 = v12.reshape(2,6)
print(m26)
c232 = v12.reshape(2,3,2)
print(c232)

v16 = np.arange(16)
m44 = v16.reshape(4,4)
print(m44)
print(np.sum(m44))
print(np.sum(m44, axis=0))
print(np.sum(m44, axis=1))