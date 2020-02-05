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

import scipy.stats as stats
slope, intercept, rvalue, pvalue, mse = stats.linregress(x, y)
print(slope, intercept, rvalue, pvalue, mse)

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(x, y)
plt.plot(range(400), np.arange(400) * slope + intercept, "ro")
plt.show()

