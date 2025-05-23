import numpy as np
import tp_function

print(np.__version__)

a1 = np.array([1,2,3,4])
print(a1)
np.random.seed(42)
rnd1 = np.random.rand(4)
print(rnd1)
print(a1 * 2)
a2 = np.array([5,6,7,8])
print(a1 * a2)
a3 = np.array([1,2,3])
# print(a2 * a3)
for i in a2:
    print(i)
print(np.sin(a2))
print(np.dot(a2, a1))
print(np.sin(0), np.sin(np.array([0,1])), np.sin(np.array([[1,2],[3,4]])))
print(np.concatenate((a2, a3)))

print(np.mean(a1))

a10 = np.arange(10)
print(a10[a10 % 2 == 0] ** 2)

np.savez("file.npz", a10=a10)
dico = np.load("file.npz")
a11 = dico["a10"]

