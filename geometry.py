import math
from typing import List
import abc


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

class Parallelogram(metaclass=abc.ABCMeta):

    def __init__(self):
        pass


    @property
    @abc.abstractmethod
    def area(self):...

class Losange(Parallelogram):

    def __init__(self):
        pass

    @property
    def area(self):
        return 1

class Rectangle(Parallelogram):

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

    def __repr__(self):
        return f"{type(self).__name__} {self._length} x {self._width}"

    def __del__(self):
        print("Destructor")

class Square(Rectangle):

    def __init__(self, side: float, origin: Point=Point(0,0)):
        super().__init__(side, side, origin)
        # Rectangle.__init__(self,side,side,origin)
        # super(Rectangle).__init__(side, side, origin)

class TriangleRectangle(Rectangle):

    def __init__(self, length: float, width: float, origin: Point=Point(0,0)):
        super().__init__(length, width, origin)

    @property
    def area(self):
        return super(Rectangle).area / 2

    def perimeter(self):
        return self._width + self._length + math.sqrt(self._width ** 2 + self._length ** 2)


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
    s1 = Square(3)
    print(s1.area)
    print(s1)

    l: List[Parallelogram] = []
    l.append(r2)
    l.append(s1)
    l.append(Losange())

    res = [p.area for p in l]
    print(sum(res))

    losange = Losange()
    print(losange)
    m = Parallelogram()
    print(m.area)

