class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width + self.length)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.area())
    print(r1.perimeter())

    r2 = Rectangle(3,2)
    print(r1 == r2)
    print(r1 is r2)

    r2 = r1
    print(r1 == r2)
    print(r1 is r2)

