import numpy as np
mat1 = np.array([[1,2],[3,4]])
mat3 = np.array([[5,6],[7,8]])
print(mat1)
print(mat1.shape)
v1 = np.arange(12)
print(v1)
print(v1.shape)
mat2 = v1.reshape(-1,3)
print(mat2)
print(mat2.shape)
v1 = mat2.reshape(-1)
print(v1)
print(np.linalg.inv(mat1))

print(np.dot(mat1, mat3))
print(mat1.dot(mat3))

print(np.sin(mat1))

c1 = 3+2j
c2 = 1j
print(c2 ** 2)

v1 = [0,1,0,0,0,0,0,0,0,0,0]
res = np.fft.fft(v1)
print(res.real)

import matplotlib.pyplot as plt
# plt.subplot(211)
# plt.plot(v1)
# plt.subplot(212)
# plt.plot(res.real)
# plt.show()

print(mat1)
print(np.sum(mat1), np.mean(mat1), np.std(mat1), np.median(mat1), np.quantile(mat1, [0.25, 0.75]))
print(np.mean(mat1, axis=1))

import cv2
res = cv2.imread("data/lans.jpg")
print(res.shape)
print(np.mean(res), np.std(res), np.min(res), np.max(res))
red = res[10:-10,10:-10,0] # Crop (10,10,10,10) sur red
green = res[:,:,1]
luminance_green = np.mean(green)
inverse = res[-1:0:-1,:,:]
nb = np.mean(inverse, axis=2)

plt.imshow(nb, cmap="gray")
plt.show()