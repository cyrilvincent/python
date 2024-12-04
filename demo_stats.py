import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

rnd = np.random.rand(100)
print(np.mean(rnd), np.std(rnd), np.var(rnd), np.median(rnd), np.quantile(rnd, 0.25), np.quantile(rnd, 0.75))

print(stats.shapiro(rnd))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(np.arange(100), rnd)
print(slope, intercept, rvalue, pvalue, stderr)

x = np.arange(100)
y = slope * x + intercept

def theorical_model(x, a, b):
    return a * x * np.sin(b * x)

coef, loss = opt.curve_fit(theorical_model, x, rnd,bounds=(-np.inf, np.inf))
print(coef) # Tuple contenant les facteurs = a et b
print(loss)

theorical_model(x, coef[0], coef[1])