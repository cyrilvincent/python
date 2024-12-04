import numpy as np
import matplotlib.pyplot as plt

signal = np.zeros(10)
signal[1] = 1

c1 = 3 + 2j
imag = 1j
print(c1 + imag)
print(imag ** 2)

result = np.fft.fft(signal)
print(result)

x = np.arange(10)
plt.subplot(211)
plt.plot(x, signal)
plt.subplot(212)
plt.plot(x, np.real(result))
plt.show()

