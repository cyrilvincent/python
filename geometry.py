class Rectangle:

    def __init__(self, length, width):
        # Attributes
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)










if __name__ == '__main__':
    r2 = Rectangle(2,3)
    r2.width = 99
    r1 = Rectangle(length=2,width=3)
    print(r1.length, r1.width)
    print(r1.area())