import math

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        # Rectangle.__init__(self, side, side)

class Triangle_rectangle(Rectangle):

    def get_area(self):
        return super().get_area() / 2

    def get_hypothenuse(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

    def get_perimeter(self):
        return self.width + self.length + self.get_hypothenuse()