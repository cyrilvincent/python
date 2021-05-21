import matplotlib.pyplot as plt
import math

# Reprenndre HouseCsv => surfaces, loyers
# x = surfaces
# y = loyers
# Nuage de points

x = range(10)
y = range(10)
plt.subplot(221)
plt.legend("demo")
# plt.plot(x, y)
plt.scatter(x, y)
# plt.bar(x, y)

serie = list(range(100))
y = [math.sin(x / 20) for x in serie]
plt.subplot(222)
plt.plot(serie, y)


y2 = [math.cos(x / 15) for x in serie]
plt.subplot(223)
plt.plot(serie, y2)

plt.subplot(224)
plt.plot(serie, y)
plt.plot(serie, y2)

plt.savefig("data/figure.png")
plt.show()
