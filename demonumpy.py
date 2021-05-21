import numpy as np

a1 = np.array([1.0,2,3])
a2 = np.array([4,5,6], dtype=np.float64)
a3 = np.arange(7,10)
a4 = np.linspace(-10,10,100)
zero = np.zeros(3)
ones = np.ones(3)

print(a1)
print(a1 + a2)
print(a1 ** 2)

print(np.sin(a1) ** 2)

f = lambda x : np.sin(x / 2) + np.cos(x / 3) + np.tanh(x) ** 2
print(f(a1))

apositive = a4[a4 > 0]
print(apositive)

res = f(a1)
res = res[res > 2.5]
print(res)

for v in res:
    print(v)

np.nan # Not a Number
# Depuis model=house.HouseCsv(...)
# Créer x = np.array(model.surfaces)
# y = np.array(model.loyers)
# loyerparm2 = y / x
# matplotlib
# Filtrer les loyerparm2 > 40


