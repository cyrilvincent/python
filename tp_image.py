import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open("data/cercle.jpg")
array = np.asarray(im).astype(np.float64)

print(array.shape)

array = array[100:-100,100:-100]
green = array[:,:,1]
green = green.T
lum = np.mean(array)
contrast = np.std(array)
print(lum, contrast)
nb = np.mean(array, axis=2)
profilH = np.mean(nb, axis=1)
plt.bar(np.arange(nb.shape[0]), profilH)
plt.show()


# Cropper l'image (enlever n pixels sur les bords)
# Obtenir le canal vert
# Transposer l'image obtenue à partir du canal vert
# Calculer la luminance et le contraste d'une image
# Convertir une image couleur en VRAI noir et blanc

dest = Image.fromarray(nb.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")