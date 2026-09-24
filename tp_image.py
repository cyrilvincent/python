from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape, array.dtype)

luminance = np.mean(array)
print(luminance)

red = array[:,:,0]
print(red.shape)

# Mettre en fonction, bonus en class
# class MyImage
# load, save, get_chanel, luminance, contrast
# crop(10)
# reduce(4) => prendre une colonne sur 2 et une ligne sur 2
# grey => transforme n&b
# negative 255 -
# profileH et V
# Bonus : normaliser l'image
# np.clip((x - mean) / std) * 255/4 + 255/2,0 ,255)


dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")