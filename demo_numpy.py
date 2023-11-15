import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.arange(4)
v3 = np.linspace(0,100, 10000)
print(v1, v2)
print(v1 * v2)
print(v2 ** 2)
print(np.sin(v1) * 2 + np.tanh(v1 / 1000))

def inc(x):
    return x + 1
print(inc(v1))

f = lambda x: 4 * x + 2
print(f(v1))

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(np.cos(mat1))

print(v1.shape, mat1.shape)
v12 = np.arange(12)
print(v12.shape)
m43 = v12.reshape(-1,3)
print(m43)
m34 = v12.reshape(3, 4)
print(m34)
c223 = v12.reshape(3,2,2)
print(c223)
m34.T + m43

import matplotlib.pyplot as plt
v4 = [0,1,0,0,0,0,0,0,0,0]
res = np.fft.fft(v4)
c1 = 3+2j
c2 = 1j
print(c2 ** 2)
print(res)
plt.plot(v4)
plt.plot(np.real(res), color="red")
plt.show()

