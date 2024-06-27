import numpy as np
import matplotlib.pyplot as plt

complex = 2 + 3j
imag = 1j
print(imag ** 2)
print(complex + imag)

signal = np.zeros(10)
signal[1] = 1
res = np.fft.fft(signal)

plt.subplot(211)
plt.plot(np.arange(10), signal)
plt.plot(np.arange(10), np.real(res))
plt.show()