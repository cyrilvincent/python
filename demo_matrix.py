import numpy as np
import matplotlib.pyplot as plt

v12 = np.arange(12)

m34 = v12.reshape(3,4)
print(m34)
print(m34.size, m34.shape)
m43 = v12.reshape(-1,3)
# print(m43 + m34)
print(np.sin(m34) * 2)

c232 = v12.reshape(2,3,2)
print(c232)

m22 = np.array([[1,2],[3,4]])
print(m22)
print(np.dot(m22, m22))

print(m22)
print(np.mean(m22, axis=1))

# cube = None
# np.mean(cube, axis=2)
# np.mean(cube, axis=0) # profil horizontal
# np.mean(cube, axis=1) # profil horizontal
# np.mean(cube) # luminosite
# np.std(cube) # contraste

print(1j ** 2)

plt.subplot(2,1,1)
signal = np.array([0,1,0,0,0,0,0,0,0,0])
plt.plot(signal)
result = np.fft.fft(signal)
plt.subplot(2,1,2)
plt.plot(np.real(result))
plt.show()


