from PIL import Image
import numpy as np

path = "data/ski.jpg"
im = Image.open(path)
array = np.asarray(im).astype(float)
print(array.shape)

lum = np.mean(array)
print(f"Luminance: {lum}")
contrast = np.std(array)
print(f"Contrast: {contrast}")

red = array[:,:,0]
nb = np.mean(array, axis = 2)
crop = array[100:-100, 100:-100]

# array = array * 0.5
# Baisser la luminosité de 10%
# np.clip(x,0,255)
norm = np.clip(((array - lum) / contrast) * 64 + 128, 0 , 255)



path_destination = "data/modified.jpg"
dest = Image.fromarray(norm.astype(np.uint8)).convert("RGB")
dest.save(path_destination)
