class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def move_relative(self, deltax: float, deltay: float):
        self.x += deltax
        self.y += deltay

class Rectangle:

    def __init__(self, length: float, width: float, origin: Point):
        # QUOI
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):


    def __init__(self, side: float, origin: Point):
        super().__init__(side, side, origin)

    def __repr__(self):
        return f"Square: {self.width}"


class TriangleRectangle(Rectangle):

    def __init__(self, length: float, width: float, origin: Point):
        super().__init__(length, width, origin)

    def area(self):
        return super().area() / 2

    def hypothenuse(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

    def perimeter(self):
        return self.width + self.length + self.hypothenuse()




class RectangleCollection:

    def __init__(self, rectangles: list[Rectangle]):
        self.rectangles = rectangles

    def total_area(self):
        return sum([r.area() for r in self.rectangles])

if __name__ == '__main__':
    # Instanciation
    p1 = Point(3,2)
    p1.move_relative(1,-1)
    assert p1.x == 4
    assert p1.y == 1
    r1 = Rectangle(3,2, p1)
    print(r1.length, r1.width)
    r2 = Rectangle(length=3, width=4, origin=Point(0,0))
    print(r2.length, r2.width)
    print(r2.area())
    print(r2.perimeter())
    r2.area() # <=>
    Rectangle.area(r2) # Très peu utilisé
    r2.origin.move_relative(1,-1)
    collection = RectangleCollection([r1, r2])
    print(collection.total_area())
    s1 = Square(3, p1)
    print(s1)
    assert s1.area() == 9
