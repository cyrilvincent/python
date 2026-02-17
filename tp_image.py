import numpy as np
from PIL import Image

im = Image.open("data/python.jpg")
array = np.asarray(im).astype(np.float64)

red = array[100:-100,:,1]


dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")

# TP
# load(path) => array
# save(array, path) => save
# get_chanel(0,1,2)
# crop(array, north, south, east, west)
# reduce(array) divise par 4 la taille : enleve 1 row sur 2 et 1 colonne sur 2
# flip(array) qui effectue une symetrie horizontal
# negative(array)