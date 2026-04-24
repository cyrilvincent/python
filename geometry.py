class Point:

    def __init__(self,x , y):
        self.x = x
        self.y = y

    def move(self,x, y):
        self.x = x
        self.y = y

    def move_rel(self, x, y):
        self.x += x
        self.y += y

class Rectangle:

    def __init__(self, width: float, length, origin: Point):
        self.width = width
        self.length = length
        self.origin = origin

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length )

if __name__ == '__main__':
    p1 = Point(2,2)
    r1 = Rectangle(3,2, p1)
    r2 = Rectangle(4,6, Point(4, -1))
    print(r1.area())
    print(r2.perimeter())
    print(r1.origin.x)
    r1.origin.move_rel(1,1)
    print(r1.origin.x)