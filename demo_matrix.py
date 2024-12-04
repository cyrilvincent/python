import numpy as np

mat22 = np.array([[1,2],[3,4]])
mat22bis = np.array([[5,6],[7,8]])
print(mat22)
print(mat22 + 1)
print(np.sin(mat22))
print(mat22 + mat22bis)
v2 = np.array([1,2])
print(mat22 + v2)

print(mat22.ndim, mat22.size, mat22.shape)

mat23 = np.array([[1,2,3],[4,5,6]])
print(mat23)
print(mat23.shape)
print(mat23[1][1], mat23[1,1])
for row in mat23:
    for col in row:
        print(col)
mat23[1,1]=5

print(np.zeros((5,5))) # np.ones
print(np.eye(5))

print(np.random.rand(2,2))

v12 = np.arange(12)
print(v12)

mat34 = v12.reshape(3,-1)
print(mat34)
mat43 = v12.reshape(-1,3)
print(mat43)
print(mat43.T.reshape(12))

print(v12.reshape(3,2,-1))

print(np.dot(mat22, mat22bis))
print(mat22.dot(mat22))

print(mat34)
print(mat34[0:-1,1:4])
print(mat34[0:-1]) # Row only
print(mat34[:,1:4]) # Column only

# Reduction
print(mat34)
print(np.sum(mat34))
print(np.sum(mat34, axis=0))
print(np.sum(mat34, axis=1))

v3 = np.array([1,2,3])
mat13 = np.array([[1,2,3]])
mat31 = np.array([[1],[2],[3]])
print(v3, v3.shape)
print(mat13, mat13.shape)
print(mat31, mat31.shape)

v5 = np.array([1,2,3,4,5])
print(v5.reshape(-1,1))

