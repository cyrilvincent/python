# pip install pillow

from PIL import Image
import numpy as np

im = Image.open("data/foret.jpg")
array =  np.asarray(im).astype(float)
print(array.shape)

red = array[::2,::2,0]
nb = np.mean(array, axis=2)

# Faire le canal vert
# Faire la fonction crop(nb:int) et on crop de nb lignes et row
# Faire le n&b
# Symetrie verticale et horizontale
# luminance (mean) + contraste (std)
# def autolum() qui ramène la luminance à 127.5
# Bonus def auto_lum_contrast = lum = 127.5, contrast = 63.75
# Bonus Superposer 2 images de même résolution, de résolution différentes (crop)

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/modified.jpg")
dest.show()