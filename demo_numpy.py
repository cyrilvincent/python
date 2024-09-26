import numpy as np

print(np.__version__)

v1 = np.array([1,2,3,4])
print(v1)
v2 = np.arange(4)
print(v2)
v3 = v1 + v2
print(v3)
print(v3 * 2)
print(v1 * v2)

print(np.sin(v1))
print(np.log2(256))

print(np.linspace(0,100,51))
print(np.zeros(10), np.ones(10), np.full(10, 99))
print(np.random.rand(10), np.random.randint(0,100, 10))

rnd = np.random.rand(1000)
print(np.mean(rnd), np.std(rnd), np.var(rnd), np.median(rnd), np.quantile(rnd, [0.01, 0.1, 0.25, 0.5, 0.99]))

salary = np.array([2000,3000,2500,1500,2200,2000000])
print(np.mean(salary), np.median(salary))