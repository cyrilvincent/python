# pip install pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape)

green = array[100:,200:-200,1]
dest = green.T

crop = 100
dest = array[crop:-crop, crop:-crop]

dest = array[::2, ::2]

lum = np.mean(array)
print(f"Luminance: {np.round(lum)}")
contrast = np.std(array)
print(f"Contrast: {np.round(contrast)}")

dest = np.mean(array, axis=2)

dest = np.clip(array + 127.5 - lum, 0, 255)

dest = ((array - lum) / contrast) * (255 / 4) + 127.5
dest = np.clip(dest, 0, 255)


dest = Image.fromarray(dest.astype(np.uint8)).convert("RGB")
dest.show()
dest.save("data/out.jpg")


# green
# transpose green.T
# cropper l'image de x pixels N,S,E,O
# Diviser l'image par 4 : 1 pixels sur 2 en lignes et colonnes
# Calculer la luminance : moyenne des pixels
# Calculer la luminance des greens
# Calculer le contraste de l'image : std
# Convertir l'image en n&b
# Corriger automatiquement la luminance d'une image : lum parfaite = 127.5 np.clip(x, 0, 255)
# Bonus : corriger automatiquement la luminance et le contraste
# Bonus 2 : Superposer 2 images
# Bonus 3 : Ranger tout dans des fonctions pour en faire un module
