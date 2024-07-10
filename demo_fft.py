import numpy as np
import matplotlib.pyplot as plt
import scipy.signa

c1 = 2 + 3j
c2 = 1j ** 2
print(c2)
print(c1 + c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0])
res = np.fft.fft(signal)
print(res)
plt.plot(signal)
plt.plot(np.real(res))
plt.show()

