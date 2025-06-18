import numpy as np
import tp_cancer

v1 = np.array([1,2,3,4])
print(v1)
v2 = np.array([5,6,7,8])
print(v1 * v2)
print(np.sin(v1))
print(np.mean(v1), np.std(v1), np.median(v1))

s = tp_cancer.CancerService()
s.load("data/cancer/data.csv")

print(np.mean(s.radius0), np.std(s.radius0), np.median(s.radius0))
print(np.mean(s.radius1), np.std(s.radius1), np.median(s.radius1))