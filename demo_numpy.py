import numpy as np

a1 = np.array([1,2,3,4,5,6], dtype=np.float64)
a2 = np.arange(1,7)
a3 = np.linspace(0,10,100)
a4 = np.zeros(6)
a4[1] = 1
a5 = np.ones(6)
print(a1 + a2)
# print(a1 + a3)
print(a1 * a5)
print(np.dot(a1, a2))
print(np.arctan(a1))

infini = np.inf
print(1/infini)
nan = np.nan

print(1j ** 2)
c1 = 1+3j
c2 = -2+3.2j
print(c1+c2)

