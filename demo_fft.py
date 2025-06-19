import numpy as np
import matplotlib.pyplot as plt

c1 = 1j
print(c1 ** 2)
c2 = 3 + 2j
print(c1 + c2)

v10 = [0,1,0,0,0,0,0,0,0,0]
plt.subplot(211)
plt.plot(np.arange(10), v10)

plt.subplot(212)
result = np.fft.fft(v10)
print(result)
plt.plot(np.arange(10), np.real(result))
plt.show()
