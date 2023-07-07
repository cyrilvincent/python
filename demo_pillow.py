from PIL import Image
import numpy as np

im = Image.open("data/mug.jpg")
array = np.asarray(im).astype(float)
print(array)

red = array[:,:,2]

lum = np.mean(array)
contrast = np.std(array)
print(lum, contrast)

array = array[100:-100, 100:-100]

nb = np.mean(array, axis=2)

norm = np.clip(((array - np.mean(array)) / np.std(array)) * 63.75 + 127.5, 0, 255)


dest = Image.fromarray(nb.astype(np.uint8)).convert("RGB")
dest.show()