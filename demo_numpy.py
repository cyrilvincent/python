import numpy as np

a1 = np.array([1.,2,3,4])
a2 = np.zeros(4)
a3 = np.ones(4)
print(a1, a2, a3)
a4 = np.arange(4)
a5 = np.arange(7,100,7)
print(a4, a5)
a6 = np.linspace(0,1,5)
a7 = np.arange(0,1.1,0.25)
print(a6, a7)
a8 = np.random.random(4)
a9 = np.random.randint(0,10,4)
print(a8, a9)

print(a1 + a3)
print(a8 + a9)
print(a8 * a9)
print(a8 * 100)

print(np.sin(0), np.sin(a8 * np.pi))

a10 = np.random.random(1000000)
print(np.sum(a10))

def f(x):
    return 2*x+1

print(f(a1))

print(1/np.inf)

print(a1.size, a1.ndim, a1.shape, a1.dtype)

# TP
# a1 = Créer un np.array de 10 flottants en dur [1,5,6,8,-3]
# a2 = créer un np.array de 10 flottants aléatoires
# Multiplier a2 par 1000
# a1 * a2
# cos(a2) * 10 + 20


