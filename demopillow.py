from PIL import Image
import numpy as np
import os

# for i in range(10):
#     path = f"data/lans{i}.jpg"
# for file in os.listdir("data"):
#     if file.endswith(".jpg"):
#         Image.open(file)

im = Image.open("data/lans.jpg")
cube = np.asarray(im)
print(np.mean(cube, axis=2))
print(cube.shape)
red = cube[:,:,0]
mean = np.mean(red)
std = np.std(red)
print(mean)
print(std)
print(np.median(red))
print(red.dtype)
red = red.astype(np.float64)
red = np.clip(red * 1.2,0,255)
im2 = Image.fromarray(red).convert("RGB")
im2.save("data/modified.jpg")
im3 = Image.fromarray(red.T).convert("RGB")
im3.save("data/transpose.jpg")

fnorm = lambda x: ((x - mean) / std) * 63.75 + 127.5
cube = cube.astype(np.float64)
imnorm = np.clip(fnorm(cube), 0, 255).astype(np.uint8)
im4 = Image.fromarray(imnorm).convert("RGB")
im4.save("data/norm.jpg")

# Charger une image en cube np
# Effectuer une transposée
# Trouver les canaux red, green, blue
# Afficher la luminance, le contraste
# Rendez l'image + lumineuse de 20%
# Normaliser la luminance l'image x - moyenne + 127.5 + clip
# Normaliser le contraste ((x - moyenne) / std) * 63.75
# Charger une 2ème image et superposer les 2 images en nb
# Charger une 3ème image et les superposer en couleur

