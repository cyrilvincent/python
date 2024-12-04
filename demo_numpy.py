import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4], dtype=np.float64)
a2 = np.arange(2.2,10.9,3.1)
a3 = np.arange(4)
a6 = a1
a4 = a1 + a3
a5 = np.tanh(a1)
print(a5)
a6 = np.zeros(10)
np.ones(10)
print(np.full(50, np.pi))

a7 = np.arange(0,10,0.1)
print(a7)
a8 = np.linspace(0,9.9,100)
print(a8)

# random
np.random.seed(42)
rnd = np.random.rand(10) * 100
print(rnd)
rnd = np.random.randint(0,100,10)
print(rnd)

# Réduction
print(a1, np.sum(a1))

# Forme
print(a1.ndim, a1.size, a1.shape)

for value in a1:
    print(value)
print(a1[0], a1[1], a1[-1])
a10 = np.arange(10)
print(a10[2:8:2])

# Save
np.savez("data.npz", toto=a10, a1=a1)

data = np.load("data.npz")
print(data)
a10 = data["toto"]
print(a10)