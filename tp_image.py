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

def range(array):
    return np.max(array) - np.min(array)

def lum(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def auto_correct(array):
    return np.clip(((array - lum(array)) / contrast(array)) * 255 / 4 + 255 / 2, 0, 255)


# range (max - min)
# lum (mean) 255/2
# contrast (std) 255/4
# auto_correct np.clip(((x - mean) / std) * 255/4 + 127.5,0,255)

if __name__ == '__main__':
    array = load("data/ski.jpg")
    red = get_chanel(array, 0)
    crop = crop(red, 20,40,60,80)
    reduce = reduce2(crop, 2)
    flip = flip(reduce)
    negative = negative(flip)
    correct = auto_correct(array)
    print(f"Range: {range(flip)}")
    print(f"Lum: {lum(negative)}")
    print(f"Contrast: {contrast(negative)}")
    save(correct, "data/out.jpg")


# TP
# load(path) => array
# save(array, path) => save
# get_chanel(0,1,2)
# crop(array, north, south, east, west)
# reduce(array) divise par 4 la taille : enleve 1 row sur 2 et 1 colonne sur 2
# flip(array) qui effectue une symetrie horizontal
# negative(array)