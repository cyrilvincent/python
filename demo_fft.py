import numpy as np
import matplotlib.pyplot as plt

complex1 = 3 + 2j
print(1j ** 2)
complex2 = 4 - 8j
print(complex1 + complex2)

signal = np.zeros(10)
signal[1] = 1

res = np.fft.fft(signal)

plt.plot(np.arange(10), signal)
plt.plot(np.arange(10), np.real(res))
plt.show()
