class Rectangle:

    def __init__(self, length: float, width: float):
        self.length= length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def _private(self):
        pass

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.length, r1.width)
    print(r1.area())
    print(r1.perimeter())
    r2 = Rectangle(4,6)