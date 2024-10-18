class MyImage:

    def __init__(self):
        self.array = None

    def load(self, path):
        self.array = ...

    def save(self, path):
        ...

    def show(self):
        ...

    def get_chanel(self, num):
        ...

    def transpose(self):
        ...

    def crop(self, north, south, east, west):
        ...

    def lum(self):
        ...

    def contrast(self):
        ...

    def auto_lum(self):
        ...

    def auto_lum_contrast(self):
        ...

    def reduce(self, factor: int):
        ...


