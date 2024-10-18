# pip install pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape)

red = array[100:,200:-200,0]

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.show()
dest.save("data/out.jpg")

# transpose .T
# green
# cropper l'image de x pixels N,S,E,O
# Diviser l'image par 4 : 1 pexels sur 2 en lignes et colonnes
# Calculer la luminance : moyenne des pixels
# Calculer la luminance des greens
# Calculer le contraste de l'image : std
# Corriger automatiquement la luminance d'une image : lum parfaite = 127.5 np.clip(x, 0, 255)
# Bonus : corriger automatiquement la luminance et le contraste
# Bonus 2 : Superposer 2 images
# Bonus 3 : Ranger tout dans des fonctions pour en faire un module
