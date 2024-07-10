from PIL import Image # pip install Pillow
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(float)
print(array.shape)

red = array[:,:,0]
nb = np.mean(array, axis=2)

crop = array[100:-100:2,100:-100:2]

lum = np.mean(array)
contrast = np.std(array)
print(lum, contrast)

auto_scale = np.clip(((array - lum) / contrast) * 64 + 127.5, 0, 255)

dest = Image.fromarray(auto_scale.astype(np.uint8)).convert("RGB")
dest.show()
