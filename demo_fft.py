import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0])
plt.plot(signal)
plt.show()
result = np.fft.fft(signal)
print(result)
plt.plot(np.real(result))
plt.show()