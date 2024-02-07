class Point:

    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y

    def move(self, x:float, y:float):
        self.x = x
        self.y = y

    def move_relative(self, x_rel:float, y_rel:float):
        self.x += x_rel
        self.y = y_rel

class Point3d(Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

class Rectangle:

    def __init__(self, length: float, width: float, origin: Point = Point()):
        # Attributes
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def move(self, x:float, y:float):
        self.origin.move(x, y)

class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)

if __name__ == '__main__':
    p1 = Point(3,2)
    r1 = Rectangle(4,5,p1)
    print(r1.origin.x)

    r2 = Rectangle(4,3,Point(3,2))

    r3 = Rectangle(4,3)
    r3.origin = p1

    r4 = Rectangle(4,3)
    r4.origin.x = 3
    r4.origin.y = 4

    r4.origin.move(5,6)

    s1 = Square(3)
    print(s1.area())
