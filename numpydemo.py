import numpy as np
mat1 = np.array([[1, 2],[3,4]])
print(mat1)
print(mat1.shape)
v = np.array([1,2,3,4])
print(v.shape)
mat1 = v.reshape(2,2)
print(mat1)
print(np.linalg.inv(mat1))

import matplotlib.pyplot as plt
import math
cloud = [math.sin(x / 100) for x in range(1000)]
plt.plot(range(1000),cloud)
plt.show()

