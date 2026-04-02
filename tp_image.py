# pip install pillow

from PIL import Image
import numpy as np

def load(path: str):
    im = Image.open(path)
    return np.asarray(im).astype(np.float64)

def save(array, path: str):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, num: int):
    return array[:,:,num]

def crop(array, north, south, east, west):
    return array[north:-south, east:-west]

def lum(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def reduce(array, factor):
    return array[::factor, ::factor]

def auto_normalize(array):
    mean = lum(array)
    std = contrast(array)
    return np.clip(((array - mean) / std) * 255 / 4 + 255 / 2, 0 ,255)

if __name__ == '__main__':
    array = load("data/ski.jpg")
    green = get_chanel(array, 1)
    cropped = crop(green, 100,200,300,400)
    print(f"Luminance: {lum(array):.1f}, contrast: {contrast(array):.1f}")
    reduced = reduce(array, 2)
    norm = auto_normalize(array)
    save(norm, "data/out.png")

# Créer la fonction load(path) -> array
# save(array, path)
# get_chanel(array, num)
# crop(array, north, suth, east, west)
# lum(array) -> float mean
# contrast(array) -> std
# reduce(array, factor) reduce(array, 2) réduit l'image de 4
# auto_normalize : Bonus ((x - mean) / std) * 255/4 + 255/2
# np.clip(x,0,255)

