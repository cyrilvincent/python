import numpy as np
from PIL import Image

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)

print(array.shape)

array = array[100:-100,100:-100]

# Cropper l'image (enlever n pixels sur les bords)
# Obtenir le canal vert
# Transposer l'image obtenue à partir du canal vert
# Calculer la luminance et le contraste d'une image
# Convertir une image couleur en VRAI noir et blanc

dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")