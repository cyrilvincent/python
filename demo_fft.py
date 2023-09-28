import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0,1,0,0,0,0,0,0,0,0,0])
a = 1j
b = 2+3j
res = np.fft.fft(signal)
print(res)



plt.plot(signal)
plt.plot(np.real(res))
plt.show()

