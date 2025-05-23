import numpy as np
import matplotlib.pyplot as plt

c1 = 3 + 2j
imag = 1j
print(imag ** 2)

print(c1 + imag)
print(np.sin(c1))

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.subplot(211)
plt.plot(signal)


result = np.fft.fft(signal)
print(result)
plt.subplot(212)
plt.plot(np.real(result))

plt.show()