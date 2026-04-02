# pip install pillow

from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)

array = array[100:-100]
red = array[:,:,0]

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")

# Créer la fonction load(path) -> array
# save(array, path)
# get_chanel(array, num)
# crop(array, north, suth, east, west)
# lum(array) -> float mean
# contrast(array) -> std
# reduce(array, factor) reduce(array, 2) réduit l'image de 4
# auto_normalize : Bonus ((x - mean) / std) * 255/4 + 255/2
# np.clip(x,0,255)