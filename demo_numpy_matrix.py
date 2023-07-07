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