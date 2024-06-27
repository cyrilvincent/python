# pip install pillow

from PIL import Image
import numpy as np



def get_chanel(n: int, array):
    return array[:,:,n]

def crop(array, north, south, east, west):
    return array[north:-south, west:-east]

def nb(array):
    return np.mean(array, axis=2)

def horizontal(array):
    return array[::-1]

def vertical(array):
    return array[:, ::-1]

def lum(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def automlum(array):
    l = lum(array)
    return np.clip(array + 127.5 - l,0,255)

def auto_lum_contrast(array):
    l = lum(array)
    c = contrast(array)
    return np.clip(((array - l) / c) * 255/4 + 127.5,0,255)


# Faire le canal vert
# Faire la fonction crop(nb:int) et on crop de nb lignes et row
# Faire le n&b
# Symetrie verticale et horizontale
# luminance (mean) + contraste (std)
# def autolum() qui ramène la luminance à 127.5
# Bonus def auto_lum_contrast = lum = 127.5, contrast = 63.75, np.clip
# Bonus Superposer 2 images de même résolution, de résolution différentes (crop)

if __name__=='__main__':
    im = Image.open("data/ski.jpg")
    array =  np.asarray(im).astype(float)
    print(array.shape)
    # dest = get_chanel(1, array)
    # dest = crop(dest,100,100,100,100)
    # dest = nb(array)
    dest = auto_lum_contrast(array)
    # dest = horizontal(dest)
    # dest = vertical(dest)
    print(dest.shape)
    print(f"Lum: {lum(dest):.0f}, contrast: {contrast(dest):.0f}")
    dest = Image.fromarray(np.round(dest).astype(np.uint8)).convert("RGB")
    dest.save("data/modified.jpg")
    dest.show()