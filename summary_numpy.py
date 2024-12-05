import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt
import scipy.integrate as integrate

np.random.seed(0)

noise = 5
def f(x):
    delta = (np.random.rand(x.size) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0, 10, 0.1)
y = f(x)


def poly3(x, a,b,c,d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

print(np.mean(y), np.std(y), np.median(y))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
weigths, loss = opt.curve_fit(poly3, x, y)
print(weigths)
weigths_xsinx, loss = opt.curve_fit(xsinx, x, y, bounds=([1,0,0],[3,1,3]))
print(weigths_xsinx)

def diff(x):
    return np.abs(2.5 * x * np.sin(0.7 * x) + 2 - (2.56 * x * np.sin(0.70 * x) + 1.98))

area, error = integrate.quad(np.sin,0, np.pi)
print(area, error)

area, error = integrate.quad(diff, 0, 10)
print(area, error)

plt.subplot(211)
plt.scatter(x, y)
plt.plot(x, slope * x + intercept, color="red")
plt.plot(x, poly3(x, weigths[0], weigths[1], weigths[2], weigths[3]), color="green")
plt.plot(x, xsinx(x, weigths_xsinx[0], weigths_xsinx[1], weigths_xsinx[2]), color="black")
plt.subplot(212)
plt.plot(x, diff(x), color="blue")
plt.show()
