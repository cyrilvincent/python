import matplotlib.pyplot as plt
import math
x = range(1000)
y = [math.sin(i/100) for i in x]
plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
y = [i * math.sin(i/100) for i in x]
plt.plot(x, y)
plt.show()