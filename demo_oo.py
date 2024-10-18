class Point:

    def __init__(self,x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_relative(self, x, y):
        self.x += x
        self.y += y


class Rectangle:

    # Constructeur
    def __init__(self, length, width, origin: Point):
        # Attributs
        # QUOI
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



if __name__ == '__main__':
    p1 = Point(0,0)
    print(p1.x, p1.y)
    p1.move(4, 5)
    p1.move_relative(-1, 2)
    print(p1.x, p1.y)
    r1 = Rectangle(3, 2, p1) # Instance = Class() : Instanciation
    print(r1.length, r1.width)
    print(r1.area(), r1.perimeter())
    print(r1.origin.x, r1.origin.y)
    r1.origin.move(0,0)
