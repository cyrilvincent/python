import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0])
a2 = np.fft.fft(a1)

plt.subplot(211)
plt.plot(a1)
plt.subplot(212)
plt.plot(np.real(a2))

plt.show()