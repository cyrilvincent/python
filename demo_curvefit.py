import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

noise = 20

def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0, 10, 0.1)
y = f(x)

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weigth2, conv2 = opt.curve_fit(poly2, x, y)
print(weigth2, conv2)

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

weigth3, conv3 = opt.curve_fit(poly3, x, y)
print(weigth3, conv3)

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

weigthsin, convsin = opt.curve_fit(xsinx, x, y)
print(weigthsin, convsin)


plt.scatter(x, y)
plt.plot(x, poly2(x, weigth2[0], weigth2[1], weigth2[2]), color="red")
plt.plot(x, poly3(x, weigth3[0], weigth3[1], weigth3[2], weigth3[3]), color="green")
plt.plot(x, xsinx(x, weigthsin[0], weigthsin[1], weigthsin[2]), color="maroon")
plt.show()
