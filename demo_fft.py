import numpy as np
import matplotlib.pyplot as plt


c1 = 3+2j
c2 = 1j
print(c2 ** 2)

plt.subplot(211)
t1 = np.array([0,1,0,0,0,0,0,0,0,0])
t2 = np.fft.fft(t1)
print(t2)
plt.plot(t1)
plt.subplot(212)
plt.plot(np.real(t2))
plt.show()

