# Créer un tableau numpy de -pi à pi avec un pas de 0.01 : a1
# Appliquer un sin : asin
# Appliquer une tanh : atanh
# Créer la fonction sigmoid (voir wikipedia)
# Créer asigmoid
# Sur atanh prendre les x € [-0.5, +0.5]
# atanh - x sur [-0.5, +0.5] ~= 0 => np.max(np.abs(atanh - x))

import numpy as np
import matplotlib.pyplot as plt

a1 = np.arange(-np.pi, np.pi, 0.01)
a_sin = np.sin(a1)
print(a_sin)
a_tanh = np.tanh(a1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

a_sigmoid = sigmoid(a1)
print(a_sigmoid)

start_index = int((np.pi - 0.5)*100)
print(start_index)
a264 = a_tanh[264:-264]
print(a264)
ax = np.arange(-0.5, 0.501, 0.01)
print(np.abs(np.max(a264 - ax)))

rnd = np.random.rand(10)
print(rnd)
print(rnd[(rnd > 0.5) & (rnd < 0.8)])

np.savez("here.npz", a264 = a264, rnd=rnd)
data = np.load("here.npz")
print(data)
print(data["rnd"])

plt.subplot(221)
plt.scatter(a1, a_tanh)
plt.subplot(222)
plt.bar(np.arange(10), rnd)
plt.subplot(223)
plt.plot(a1, a_sigmoid)
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery-nogrid')

# # make data: correlated + noise
# np.random.seed(1)
# x = np.random.randn(5000)
# y = 1.2 * x + np.random.randn(5000) / 3

# # plot:
# fig, ax = plt.subplots()

# ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))

# ax.set(xlim=(-2, 2), ylim=(-3, 3))

# plt.show()

