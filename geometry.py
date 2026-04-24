class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length )

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    r2 = Rectangle(4,6)
    print(r1.area())
    print(r2.perimeter())