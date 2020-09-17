import pandas
import numpy as np
import matplotlib.pyplot as plt

dataframe = pandas.read_csv("data/mesures.csv")

errors = np.abs(dataframe.VM - dataframe.VT)

plt.subplot(211)
plt.plot(dataframe["T"], dataframe.VM)
plt.subplot(212)
plt.plot(dataframe["T"], errors)
plt.scatter(dataframe[errors > 1]["T"], errors[errors > 1],c="red")
plt.show()

print(errors[errors > 1])

x = 3+2j
x = 1j ** 2
print(x)