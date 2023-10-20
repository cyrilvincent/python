import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

print(np.__version__)

v1 = np.array([1, 2, 3, 4])
v2 = np.arange(4)
# v3 = np.linspace(0,1,101)

print(v1)
print(v2)
# print(v3)

v3 = v1 * v2
print(v3)
# Scalar
v3 = v1.dot(v2)
print(v3)

print(np.sin(v1))

print(np.median(v1))

print(3 * v1)

mat1 = np.array([[1,2], [3,4]])
print(mat1)
print(mat1.shape)

v1 = np.arange(12)
mat1 = v1.reshape(3,4)
print(mat1)
print(mat1.reshape(4,3))
print(mat1.reshape(2,-1))
print(mat1.reshape(1,-1))
print(mat1.reshape(-1,1))
print(mat1.T)

mat1 = np.array([[1,2], [3,4]])
print(np.linalg.inv(mat1))

def linear(x):
    return 2*x+3

print(linear(mat1))


c1 = 3+2j
print(1j ** 2)
v1 = [0,1,0,0,0,0,0,0,0,0]
res = np.fft.fft(v1)
print(res)

plt.figure(1)
plt.subplot(211)
plt.plot(np.arange(10), v1)
plt.subplot(212)
plt.plot(np.arange(10), np.real(res), color="red")
plt.interactive(True)
plt.show()

import demo_file
loyers, surfaces = demo_file.load_csv("data/house/house.csv")
slope, intercept, r1, pvalue, loss = stats.linregress(surfaces, loyers)
print(slope, intercept, r1, pvalue, loss)
plt.scatter(surfaces, loyers)
x = np.arange(400)
plt.figure(2)
plt.plot(x, slope * x + intercept)
plt.interactive(False)
plt.show()
