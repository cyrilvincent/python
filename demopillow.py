from PIL import Image
import numpy as np

im = Image.open("data/lans.jpg")
cube = np.asarray(im)
print(np.mean(cube, axis=2))
print(cube.shape)
red = cube[50:-50,50:-50,0]
print(np.mean(red))
print(np.std(red))
print(np.median(red))
print(red.dtype)
red = red.astype(np.float64)
red = np.clip(red + 20,0,255)
im2 = Image.fromarray(red).convert("RGB")
im2.save("data/modified.jpg")

# Charger une image en cube np
# Effectuer une transposée
# Trouver les canaux red, green, blue
# Afficher la luminance, le contraste
# Rendez l'image + lumineuse de 20%
# Normaliser la luminance l'image x - moyenne + 127.5 + clip
# Normaliser le contraste ((x - moyenne) / std) * 63.75
# Charger une 2ème image et superposer les 2 images en nb
# Charger une 3ème image et les superposer en couleur

