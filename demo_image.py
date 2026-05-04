import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# pip install pillow

im = Image.open("data/cercle.jpg")
array = np.asarray(im).astype(np.float64)

print(array.shape)

red = array[:,:,0]
print(red.shape)

cropped = array[50:-50,50:-50]
nb = np.mean(array, axis=2)

profilH = np.mean(nb, axis=0)
print(profilH.shape)

plt.plot(profilH)
plt.show()

print(np.mean(array))

dest = Image.fromarray(nb.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")