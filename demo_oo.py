import math

class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def move_rel(self, x: float, y: float):
        self.x += x
        self.y += y

class Point3d(Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

class Rectangle:

    def __init__(self, length: float, width: float, origin: Point):
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    

class Square(Rectangle):

    def __init__(self, side, origin):
        super().__init__(side, side, origin)

class TriangleRectangle(Rectangle):

    def __init__(self, length, width, origin):
        super().__init__(length, width, origin)

    def area(self):
        return super().area() / 2
    
    def hypothenuse(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)
    
    def perimeter(self):
        return self.width + self.length + self.hypothenuse()

    
class RectangleCollection:

    def __init__(self, rectangles: list[Rectangle] = []):
        self.rectangles = rectangles

    def add(self, rectangle: Rectangle):
        self.rectangles.append(rectangle)

    def total_area(self):
        return sum([r.area() for r in self.rectangles])
    

if __name__ == "__main__":
    p1 = Point(4,-1)
    r1 = Rectangle(2,3,p1)
    assert 6 == r1.area()
    assert 10 == r1.perimeter()
    r2 = Rectangle(3,4,Point(0,1))
    r1.origin.move_rel(1, -1)
    assert 5 == r1.origin.x
    assert -2 == r1.origin.y
    rc = RectangleCollection()
    rc.add(r1)
    rc.add(r2)
    print(rc.total_area())
    s1 = Square(3)
    
