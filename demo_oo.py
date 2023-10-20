class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle): # Héritage

    def __init__(self, side):
        super().__init__(side, side)





class Toto:
    pass
