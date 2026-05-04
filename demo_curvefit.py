import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

noise = 10
def f(x):
    delta = (np.random.rand(len(x)) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0, 10, 0.1)
y = f(x)

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 +c * x + d

weights, conv = opt.curve_fit(poly3, x, y) #,bounds=((1,-np.inf, -10, 0),(4,np.inf, 10, 4)))
print(weights, conv)

def poly4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 +c * x ** 2 + d * x + e

weights4, conv4 = opt.curve_fit(poly4, x, y)
print(weights4, conv4)

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

weightsxsinx, convxsinx = opt.curve_fit(xsinx, x, y)
print(weightsxsinx, weightsxsinx)



plt.scatter(x, y)
plt.plot(x, poly3(x, weights[0], weights[1], weights[2], weights[3]), color="red")
plt.plot(x, poly4(x, weights4[0], weights4[1], weights4[2], weights4[3], weights4[4]), color="green")
plt.plot(x, xsinx(x, weightsxsinx[0], weightsxsinx[1], weightsxsinx[2]), color="maroon")
plt.show()