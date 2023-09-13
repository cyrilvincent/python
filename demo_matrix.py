import numpy as np

mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[0,1],[1,0]])
v1 = np.array([1,2])
print(mat1)

print(mat1 * 2)
print(mat1 * v1)
print(mat1 * mat2)

print(mat1.ndim, mat1.size, mat1.shape)

v1 = np.array([1,2,3,4])
mat3 = v1.reshape(2,2)
print(mat3)

v2 = np.arange(12)
mat4 = v2.reshape(4,3)
v3 = mat4.reshape(12)
v2.reshape(-1,3)
print(mat4)

mat1 = np.array([[1,2],[3,4]])
print(mat1.sum(), np.sum(mat1))
print(mat1)
print(mat1.sum(axis=0), mat1.sum(axis=1))

cube = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]]])
print(cube.shape)

