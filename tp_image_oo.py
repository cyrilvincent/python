from PIL import Image
import numpy as np

class MyImage:

    def __init__(self):
        self.array = None

    def load(self, path):
        im = Image.open(path)
        self.array = np.asarray(im).astype(np.float64)

    def save(self, path):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def show(self):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.show()

    def get_chanel(self, num):
        self.array = self.array[:,:,num]

    def transpose(self):
        self.array = self.array.T

    def crop(self, north, south, east, west):
        self.array = self.array[north:-south,west:-east]

    def lum(self):
        return np.mean(self.array)

    def contrast(self):
        return np.std(self.array)

    def auto_lum(self):
        self.array = np.clip(self.array + 127.5 - self.lum(), 0, 255)

    def auto_lum_contrast(self):
        self.array = ((self.array - self.lum()) / self.contrast()) * (255 / 4) + 127.5
        self.array = np.clip(self.array, 0, 255)

    def reduce(self, factor: int):
        self.array = self.array[::factor, ::factor]

if __name__ == '__main__':
    image = MyImage()
    image.load("data/ski.jpg")
    image.get_chanel(2)
    # image.transpose()
    image.crop(100,200,300,400)
    print(image.lum())
    image.auto_lum_contrast()
    image.reduce(2)
    image.save("data/out.jpg")
    image.show()

