import numpy as np

mat23 = np.array([[1,2,3],[4,5,6]])
mat22 = np.array([[1,2],[3,4]])
v3 = np.array([1,2,3])
print(mat23 * v3)
mat13 = np.array([[1,2,3]])
print(mat13)
mat31 = mat13.T
print(mat31)
print(mat23.size, mat23.shape)
print(mat13.shape, mat31.shape)

v12 = np.arange(12)
print(v12)
m34 = v12.reshape(3,-1)
print(m34)
m43 = v12.reshape(-1, 3)
print(m43)
c232 = v12.reshape(2, 3, 2)
print(c232)
mat121 = v12.reshape(12,1)
print(mat121)
v12 = m34.reshape(-1)
print(v12)

vinf = np.array([1,2,3,np.inf,5])
print(vinf * 2)
vnan = np.array([1,2,np.nan,4])
print(np.mean(vnan))
print(np.nanmean(vnan))

print(mat23)
print(np.sum(mat23))
print(np.sum(mat23, axis=0))
print(np.sum(mat23, axis=1))

# def affine(x):
#     return 2 * x + 3

affine = lambda x: 2 * x + 3

print(affine(v12))
print(v12 * 2 + 3)

