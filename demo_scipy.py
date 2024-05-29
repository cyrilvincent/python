import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

x = np.arange(0, 2*np.pi, 0.03)
y = np.sin(x)
plt.scatter(x, y)
plt.show()

f = lambda x,a,b: a * np.sin(b * x)
res = opt.curve_fit(f, x, y)
print(res[0])

f = lambda x: np.abs(np.sin(x)) #f(x) = |sin(x)|

res = integrate.quad(f, 0, 2 * np.pi)
print(res)
