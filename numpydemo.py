import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.array(np.arange(1,5))
print(v2)
print(v1 + v2)
print(v1 * v2) # membre à membre
print(v1.dot(v2)) # * scalaire
print(np.sin(v1) * v2)

c1 = 4 + 2j
print(1j ** 2)

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(v1.shape)
print(mat1.shape)
v1 = np.array([1,2,3,4])
mat2 = v1.reshape(2,2)
print(mat2)
print(mat2.T)
print(np.linalg.inv(mat2))

v1 = np.zeros(10)
v1[1]=1
print(v1)
res = np.fft.fft(v1)
print(res)

import matplotlib.pyplot as plt
# plt.subplot(211)
# plt.plot(np.real(res))
# plt.subplot(212)
# plt.plot(np.imag(res))
# plt.show()

import pandas as pd
df = pd.read_csv("data/house.csv")
df = df[df.surface < 250]
df = df[np.abs(df.loyer / df.surface - 37.5) < 3 * 9.62 ]
print(df)
plt.scatter(df["surface"], df["loyer"])
print(np.mean(df["loyer"] / df["surface"]))
print(np.median(df["loyer"] / df["surface"]))
print(np.std(df["loyer"] / df["surface"]))
plt.show()


