import numpy as np

a1 = np.array([1.,2,3,4], dtype=np.uint8)
print(a1.dtype)
a2 = np.arange(0,10,2)
print(a2)
a3 = np.linspace(0,10,5)
print(a3)

rnd = np.random.rand(10)
print(rnd)
rnd = np.random.randint(0,100,10)
print(rnd)

print(np.sin(a1) ** 2)

a3 = np.array([5,6,7,8])
print(a1 + a3)

print(np.mean(a3))

print(a3.dtype, a3.ndim, a3.size, a3.shape)

a10 = np.arange(100) * 2
print(a10)
n=5
print(a10[n:-n:2])
print(a10[a10 < 50])

temp = np.random.randint(18, 24, 10)

np.mean(temp)
temp.mean()

rh = np.random.rand(10)
print(temp)
print(rh)
filter = rh < 0.5
print(filter)
print(temp[filter])


