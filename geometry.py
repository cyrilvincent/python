class Point:

    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

class Rectangle:

    nb = 0

    def __init__(self, length=0, width=0, origin=Point()):
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def move(self, point):
        self.origin = point

if __name__ == '__main__':
    p1 = Point(4,-3)
    r1 = Rectangle(3,2,p1)
    print(r1.area())
    print(r1.perimeter())
    r2 = Rectangle(3,2,Point(5,-8))
    print(r1 is r2)
    print(Rectangle.nb)
    Rectangle.nb += 1
    print(Rectangle.nb)
    print(r1.origin.x, r1.origin.y)
    r1.move(Point(-1,-2))
    print(r1.origin.x, r1.origin.y)