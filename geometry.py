class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, length, width, origin:Point = Point(0,0)):
        self._length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self._length * self.width

    def perimeter(self):
        return 2 * (self.width + self._length)

    def __repr__(self):
        return f"Rectangle({self._length},{self.width})"




if __name__ == '__main__':
    r1 = Rectangle(3,2, Point(2,-1))
    r1._length = 2
    print(r1)
    print(r1.area())
    print(r1.perimeter())

    r1.origin.move(5,5)

    r2 = Rectangle(3,2)
    print(r1 == r2)
    print(r1 is r2)

    r2 = r1
    print(r1 == r2)
    print(r1 is r2)

