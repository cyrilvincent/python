import numpy as np
import matplotlib.pyplot as plt

v1 = np.zeros(10)
v1[1] = 1

plt.subplot(211)
plt.plot(v1)


res = np.fft.fft(v1)
print(res)
plt.subplot(212)
plt.plot(np.real(res))
plt.show()



