import numpy as np
from PIL import Image

im = Image.open("data/python.jpg")
array = np.asarray(im).astype(np.float64)

red = array[100:-100,:,1]


dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")

def load(path):
    im = Image.open(path)
    return np.asarray(im).astype(np.float64)

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, nb):
    return array[:,:,nb]

def crop(array, north, south, east, west):
    return array[north:-south, east:-west]

def reduce2(array, ratio):
    return array[::ratio, ::ratio]

def flip(array):
    return array[::-1]

def negative(array):
    return 255 - array

if __name__ == '__main__':
    array = load("data/python.jpg")
    red = get_chanel(array, 0)
    crop = crop(red, 20,40,60,80)
    reduce = reduce2(crop, 2)
    flip = flip(reduce)
    negative = negative(flip)
    save(negative, "data/out.jpg")


# TP
# load(path) => array
# save(array, path) => save
# get_chanel(0,1,2)
# crop(array, north, south, east, west)
# reduce(array) divise par 4 la taille : enleve 1 row sur 2 et 1 colonne sur 2
# flip(array) qui effectue une symetrie horizontal
# negative(array)