import matplotlib
import random
import matplotlib.pyplot as plt

print(matplotlib.__version__)

x = [0,1,2,3,4,5,6,7,8,9]
y= []
for i in range(10):
    y.append(random.randint(0,100))

plt.subplot(221)
plt.plot(x, y,"bo-")
plt.subplot(222)
plt.bar(x, y)
plt.show()