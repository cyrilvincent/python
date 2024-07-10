import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)

print(mat1.size, mat1.shape, mat1.ndim)

v12 = np.arange(12)
mat43 = v12.reshape(4,3)
print(mat43)
mat112 = v12.reshape(1,12)
mat121 = v12.reshape(12,1)
print(mat112)
print(mat121)
mat34 = v12.reshape(-1, 4)
print(mat34)
cube232 = v12.reshape(2,3,-1)
print(cube232)
print(cube232.reshape(6,-1))

print(mat1, np.sum(mat1))
print(np.sum(mat1, axis=1))