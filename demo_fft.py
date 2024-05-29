import scipy.fft as fft
import numpy as np
import matplotlib.pyplot as plt

y = np.array([0,1,0,0,0,0,0,0,0,0,0,0])
yt = fft.fft(y)
print(yt)
imag = 0+1j
print(imag ** 2)
plt.plot(y)
plt.plot(np.real(yt))
plt.show()