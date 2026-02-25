import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

# a1 = np.array([0,1,2,3])
# infini = np.inf
# print(1/a1)

print(1j ** 2)

c1 = 0+1j
c2 = -3+2j
print(c1 + c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0])
result = np.fft.fft(signal)
plt.subplot(2,1,1)
plt.plot(signal)
plt.subplot(2,1,2)
plt.plot(np.real(result))
plt.show()