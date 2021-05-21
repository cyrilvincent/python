import numpy as np
import house
import matplotlib.pyplot as plt

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

mat1 = np.array([[1,2,3],[4,5,6]])
mat1 = mat1
print(mat1)
print(mat1.shape)
v = mat1.reshape(6)
mat1 = v.reshape(2,3)


mat1 = np.array([[1,2],[3, 4]])
print(mat1)
print("Sum", np.sum(mat1))
print("Sum axis0", np.sum(mat1, axis=0))
print("Sum axis1", np.sum(mat1, axis=1))






# Depuis model=house.HouseCsv(...)
# Créer x = np.array(model.surfaces)
# y = np.array(model.loyers)
# loyerparm2 = y / x
# matplotlib
# Filtrer les loyerparm2 > 40

model = house.HouseCsv("data/house.csv")
model.load()
x = np.array(model.surfaces)
y = np.array(model.loyers)
plt.scatter(x, y)
plt.show()
loyerparm2 = y / x
np.set_printoptions(precision=1)
print(loyerparm2[loyerparm2 > 60])




