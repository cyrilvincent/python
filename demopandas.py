import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/mesures.csv")
print(dataframe)
vm = dataframe.VM
print(vm.values)

plt.subplot(311)
plt.plot(dataframe.VT)
plt.subplot(312)
plt.plot(dataframe.VM)
diff = np.abs(dataframe.VM - dataframe.VT)
plt.subplot(313)
plt.plot(diff)
plt.show()

delta = 1
print(diff[diff > delta])
print(dataframe.VM[diff > delta])
print(dataframe.VT[diff > delta].values)

diff.to_excel("data/diff.xlsx")