import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)
print(m1.shape)
m2 = np.array([[1,2,3],[4,5,6]])
print(m2)
print(m2.shape)
print(m2.T)
m3 = np.array([[1,2,3]])
print(m3)
print(m3.shape)
m3T = m3.T
print(m3T)
print(m3T.shape)

v1 = np.arange(12)
m1 = v1.reshape(4,3)
print(m1)
m2 = v1.reshape(3,4)
print(m2)
m3 = v1.reshape(1,12)
print(m3)