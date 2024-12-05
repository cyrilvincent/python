import datetime

class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_rel(self, x, y):
        self.x += x
        self.y += y

class Rectangle:

    def __init__(self, length, width, coord):
        self.length = length
        self.width = width
        self.coord = coord

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):

    def __init__(self, side, coord):
        super().__init__(side, side, coord)




if __name__ == '__main__':
    c1 = Coord(-2,4)
    c2 = Coord(1,0)
    r1 = Rectangle(3,2,c1)
    r1.coord.move_rel(3,4)
    print(r1.coord.x, r1.coord.y)
    print(r1.length, r1.width)
    print(r1.area(), r1.perimeter())
    r2 = Rectangle(4,5, Coord(6,1))
    print(r2.area(), r2.perimeter())
    s1 = Square(3, c1)
    print(s1.area())

