class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def move_relative(self, x: float, y: float):
        self.x += x
        self.y += y



class Rectangle:

    def __init__(self, length: float, width: float, origin: Point=Point(0,0)):
        """
        Rectangle
        :param length:
        :param width:
        """
        self._length = length
        self._width = width
        self.origin = origin

    @property
    def area(self):
        """
        Aire du rectangle
        :return:
        """
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def __del__(self):
        print("Destructor")

if __name__ == '__main__':
    p1 = Point(4,0)
    r1 = Rectangle(2,3, p1)
    print(r1)
    assert r1.area == 6
    assert r1.perimeter() == 10
    # Rectangle.area(r1) # <=> r1.area()
    r2 = Rectangle(4,3, Point(-2, 1))
    r2._length += 1
    r2.origin.move(1,1)
    r1 = None
    r1 = r2
    del(r1)
