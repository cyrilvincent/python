import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4])
print(a1)
print(np.full(4, np.pi))
a2 = np.arange(0, 10, 0.1)
print(a2)
a3 = np.linspace(0,9.9999,100)
print(a3)
np.random.seed(42)
a4 = np.random.rand(10)
print(a4)
a5 = np.random.randint(0,100,10)
print(a5)

a1 = np.array([1.,2,3,4], dtype=np.uint8)
a2 = np.array([5,6,7,8], dtype=np.float64)

print(a1 + 252)

print(a1.ndim, a1.size, a1.shape, a1.dtype)
a2.astype(np.uint8)

a3 = a1 + a2
print(a3)
print(a1 / a2)
print(np.sum(a1))

print(np.round(np.random.rand(10), 1) * 10)

a4 = np.arange(10)
print(a4)
print(a4[-1])
# Slice
print(a4[::-2])

a5 = np.arange(0, 4*np.pi, 0.01)
a6 = 2*np.sin(a5)+1

def f(x):
    return 2 * np.sin(x) + 1

print(f(a5))

print(np.max(np.array([1,2,np.nan])))


