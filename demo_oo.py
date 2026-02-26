class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def translate(self, x: float, y: float):
        self.x += x
        self.y += y

class Rectangle:

    def __init__(self, length: float, width: float, coord: Point):
        self.length= length
        self.width = width
        self.coord = coord

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def _private(self):
        pass

if __name__ == '__main__':
    p0 = Point(2,3)
    r1 = Rectangle(3,2,p0)
    print(r1.length, r1.width)
    print(r1.area())
    print(r1.perimeter())
    r2 = Rectangle(4,6,Point(4,2))
    r2.coord.translate(1,1)
    p1 = Point(0, 0)
    p1.move(3,2)
    p1.translate(2, -1)
    assert p1.x == 5
    assert p1.y == 1
    print(type(p1))