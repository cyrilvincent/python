import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)
m_one = np.ones((2,2))
print(m_one)

m_random = np.random.random((5,5)) * 100
print(m_random)

m2 = np.array([[1,2,3],[4,5,6]])
print(m2.ndim, m2.size, m2.shape)
print(m2.T)

# Reshape, axis, slice, clip, linalg, fft

m3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(m3)
print(m3.shape)
print(m3.reshape(2,6))
print(m3.reshape(6,2))
print(m3.reshape(12))
print(m3.reshape(3,-1))
print(m3.reshape(3,2,2))

# Axis
print(m1)
print(m1[:,0])
print(m1[1,0])
#print(m1[10:20,15:35])

print(m1)
print(np.sum(m1))
print(np.sum(m1, axis=0))
print(np.sum(m1, axis=1))

print(np.clip(np.array([1,2,3,99,4]),0,4))