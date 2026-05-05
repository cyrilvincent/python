import numpy as np

print(np.__version__)

v4 = np.array([1,2,3,4], dtype=np.float64)
print(v4)
v4bis = np.array([5,6,7,8])

print(np.sum(v4))
for v in v4:
    print(v)

print(v4 + v4bis)

v10 = np.arange(10)
print(v10)

# x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
print(x)

rnd = np.random.rand(10) * 100
rnd2 = np.random.randint(0, 100, 10)
print(rnd)

print(rnd.ndim, rnd.size, rnd.shape)

v25 = np.arange(0,100,4)
print(v25)
for v in v25:
    print(v)
for i in range(len(v25)):
    print(v25[i])
print(v25[10:20:2])

v10 = np.arange(10)
v20_30 = np.arange(20, 30)
filter = v10 % 2 == 0
print(filter)
print(v20_30[filter])

t = np.linspace(0, 10, 100)
ac = np.sin(x)
filter = ac > 0
print(t[filter])  # print(t[ac > 0])

