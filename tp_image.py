from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageManagement:

    def load(self, path):
        im = Image.open(path)
        array = np.asarray(im).astype(np.float64)
        return array

    def save(self, array, path):
        dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def luminance(self, array):
        return np.mean(array)

    def contrast(self, array):
        return np.std(array)

    def get_chanel(self, array, num):
        return array[:,:,num]

    def crop(self, array, north, south, east, west):
        return array[north:-south, west:-east]

    def reduce(self, array, nb):
        step = int(nb ** 0.5)
        return array[::step, ::step]


    def grey(self, array):
        return np.mean(array, axis=2)

    def negative(self, array):
        return 255 - array


    def profil(self, array, horizontal=True):
        if horizontal:
            return np.mean(array, axis=0)
        else:
            return np.mean(array, axis=1)

    def normalize(self, array):
        mean = self.luminance(array)
        std = self.contrast(array)
        return np.clip(((array - mean) / std) * 255/4 + 127.5,0 ,255)



if __name__ == '__main__':
    im = ImageManagement()
    array = im.load("data/ski.jpg")
    print(f"Luminance: {im.luminance(array):.2f}")
    print(f"Contrast: {im.contrast(array):.2f}")
    red = im.get_chanel(array, 0)
    cropped = im.crop(array, 100, 200, 300, 400)
    reduced = im.reduce(array, 4)
    grey = im.grey(array)
    negative = im.negative(array)
    normalized = im.normalize(array)
    im.save(normalized, "data/out.png")
    array = im.load("data/cercle.jpg")
    profileh = im.profil(array)

    plt.plot(profileh)
    plt.show()



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


