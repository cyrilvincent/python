import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

mat1 = np.random.rand(8,8)
mat2 = np.random.rand(8,8)
step = 10
for k in range(step + 1):
    print(k)
    mat = np.zeros((8,8))
    for row in range(8):
        for col in range(8):
            mat[row,col] = mat1[row, col] + (mat2[row, col] - mat1[row, col]) * k / step
    fig, ax = plt.subplots()
    ax.matshow(mat)
    for (i, j), z in np.ndenumerate(mat):
        ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center')
    # plt.colorbar()
    fig.savefig(f"data/images/mat{k}.png")
plt.show()

with imageio.get_writer("data/images/animation.gif", fps=2) as writer:
    for i in range(step):
        image = imageio.imread(f"data/images/mat{i}.png")
        writer.append_data(image)




