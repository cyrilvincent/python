import numpy as np
import matplotlib.pyplot as plt

imag = 1j
print(imag ** 2)
complex = 3 - 2j
print(complex + imag)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0])
result = np.fft.fft(signal)
print(result)

plt.subplot(2,1,1)
plt.plot(signal)
plt.subplot(2,1,2)
plt.plot(np.real(result))
plt.show()