class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    nb = 0

    def __init__(self, length, width, coord: Point): # Constructeur
        self.length = length  # Attributs
        self.width = width
        self.coord = coord
        Rectangle.nb += 1

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 *(self.width + self.length)

    def __del__(self):
        Rectangle.nb -= 1

if __name__ == '__main__':
    p1 = Point(2,-3)
    print(p1.x, p1.y)
    p1.move(5,4)
    print(p1.x, p1.y)
    r1 = Rectangle(3,2, p1)
    r1.coord.move(0,0)
    print(r1.nb)
    print(r1.area())
    print(r1.perimeter())
    r2 = Rectangle(4,5, Point(2,3))
    print(r2.nb)
    del(r2)
    print(Rectangle.nb)
