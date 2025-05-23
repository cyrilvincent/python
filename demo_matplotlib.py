import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(100)
# y = np.arange(100)
#
# plt.plot(x, y)
# plt.show()

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)


plt.subplot(211)
plt.title("Demo")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.plot(x, y, label="sin")
plt.scatter(x, y2, color="red", label="cos")
plt.legend()
plt.subplot(212)
plt.plot(x, y2, label="cos")
plt.legend()
plt.show()

#
# plt.style.use('_mpl-gallery')
#
# # make data
# np.random.seed(1)
# x = np.linspace(0, 8, 16)
# y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
# y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))
#
# # plot
# fig, ax = plt.subplots()
#
# ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
# ax.plot(x, (y1 + y2)/2, linewidth=2)
#
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()