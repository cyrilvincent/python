import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y1 = np.sin(x)
y2 = x * np.sin(x)

filter = y2 > 0
print(filter)
y1_filtered = y1[filter]

other_filter = y1[(y1 < 0) & (y2 > 0)] # & = AND, | = OR ! = NOT
other_x = x[(y1 < 0) & (y2 > 0)]

plt.plot(other_x, other_filter)
plt.show()
