class Rectangle:

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.length)
    print(r1.area())
    print(r1.perimeter())
    r2 = Rectangle(3,2)
    print(r1 is r2)