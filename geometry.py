class Rectangle:

    def __init__(self, length: float, width: float=0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    r2 = Rectangle(1)
    print(r1.area())