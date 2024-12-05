import datetime

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    # def __add__(self, other): # +
    #     return self.price + other.price

    # def __eq__(self, other): # ==
    #
    # def __lt__


if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.length, r1.width)
    print(r1.area(), r1.perimeter())
    r2 = Rectangle(4,5)
    print(r2.area(), r2.perimeter())

