import numpy as np

a1 = np.arange(1000)
a2 = np.arange(10,100,0.01)

np.savez("data.npz",a1 = a1, a2 = a2)

data = np.load("data.npz")
a1 = data["a1"]
a2 = data["a2"]

print(a1)
print(a2)


