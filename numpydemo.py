import numpy as np

a = np.array([1,2,3,4])
b = np.arange(4)
print(a * b)

import sqlite3

def rows_to_dict(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

conn = sqlite3.connect("data/house.db3")
cursor = conn.cursor()
cursor.execute("select * from house")
dict = rows_to_dict(cursor)

x = [row["surface"] for row in dict]
y = [row["loyer"] for row in dict]
x = np.array(x)
y = np.array(y)
res = y / x
print(np.mean(res))
print(np.std(res))
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()

c1 = 3j+2
c2 = 1j
print(c2 ** 2)
print(np.real(c1))
print(np.imag(c1))
print(c1 + c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0])
res = np.fft.fft(signal)
print(res)
plt.plot(np.real(res))
plt.show()