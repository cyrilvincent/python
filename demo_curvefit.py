import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

noise = 10
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0,10 , 0.1)
y = f(x)

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x +d
def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

weight3, conv3 = opt.curve_fit(poly3, x, y)
weightsin, convsin = opt.curve_fit(xsinx, x, y, bounds=([1,-np.inf, -np.inf], [4, np.inf, 4]))

print(weightsin)
print(convsin)

plt.scatter(x, y)
plt.plot(x, poly3(x, weight3[0], weight3[1], weight3[2], weight3[3]), color="red", label="poly3")
plt.plot(x, xsinx(x, weightsin[0], weightsin[1], weightsin[2]), color="black", label="xsinx")
plt.legend()
plt.show()