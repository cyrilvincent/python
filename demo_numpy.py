import numpy as np

a1 = np.array([1.0,2,3,4])
print(a1)
print(a1.size, a1.dtype)
a2 = np.arange(4, dtype=np.float64)
print(a2)
print(a1 + a2)
a3 = np.sin(a1 + a2)
print(a3)

m1 = np.array([[1,2],[3,4]])
print(m1)
print(m1.shape)
a4 = np.arange(1,13)
print(a4, a4.shape)
print(a4.reshape(3,2,2))
m2 = np.array([[1,1],[2,2]])
print(m1 + m2)