import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as integrate

np.random.seed(0)
noise = 1
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    # f(x) = 2.5x.sin(0.7x)+2
    return  2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0, 10, 100)
plt.scatter(x, f(x))


# f(x) = ax.sin(bx)+c
model = lambda x, a, b, c: a * x * np.sin(x * b) + c
model4 = lambda x,a,b,c,d,e: a*x**4 + b*x**3 + c*x**2 + d*x + e
# def model(x,a,b,c,d):
#     return a * x * np.sin(x * b) + c

weigths, conv = opt.curve_fit(model, x, f(x))
print(weigths)
print(conv)

weigths4, conv4 = opt.curve_fit(model4, x, f(x))
print(weigths4)
print(conv4)


diff = lambda x,a,b,c,a4,b4,c4,d4,e4: np.abs(model(x,a,b,c)-model4(x,a4,b4,c4,d4,e4))
area = integrate.quad(diff,2,4, args=(weigths[0] , weigths[1], weigths[2], weigths4[0] , weigths4[1], weigths4[2], weigths4[3], weigths4[4]))
print(area)


x = np.linspace(0, 10, 100)
plt.plot(x, model(x, weigths[0] , weigths[1], weigths[2]), color="red")
plt.plot(x, model4(x, weigths4[0] , weigths4[1], weigths4[2], weigths4[3], weigths4[4]), color="green")
plt.show()