import numpy as np
import matplotlib.pyplot as plt

a = np.array([0,1,0,0,0,0,0,0,0,0,0,])

res = np.fft.fft(a)

plt.subplot(211)
plt.plot(a)
plt.subplot(212)
plt.plot(np.real(res))
plt.show()
