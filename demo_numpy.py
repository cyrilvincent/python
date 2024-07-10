import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.arange(0,10,0.1)
a3 = np.linspace(0, 9.9, 100)
np.random.seed(42)
rnd = np.round(np.random.rand(10) * 100, 0)
rnd2 = np.random.randint(0,100, 10)
print(rnd)

print(a1 + 1)
a4 = np.arange(4, dtype=np.float64)
print(a1 * a4)
print(np.tanh(a1) * 2)

print(np.max(a4))

print(a4.size, a4.ndim, a4.shape, a4.dtype)

a5 = np.arange(100)

a6 = np.array([1,2,3])
print(a6[[True, False, True]])
filter = (a5 % 3 == 0) & (a5 < 50)

f = lambda x: x ** 2

def f2(x):
    return x ** 2

res = f2(a5[filter])

np.savez("data.npz", res=res, a4=a4)
file = np.load("data.npz")
print(file["res"])

rnd = np.random.rand(10000)
print(np.mean(rnd), np.std(rnd), np.median(rnd), np.quantile(rnd, [0.01,0.1,0.25,0.5,0.75]))



