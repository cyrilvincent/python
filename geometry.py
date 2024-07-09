import abc

class Polygon(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def area(self): ...


class Rectangle(Polygon):

    def __init__(self, length: float, width: float=0):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def _perimeter(self):
        return 2 * (self.length + self.width)

    def __del__(self):
        pass

class Square(Rectangle):

    def __init__(self, side: float):
        if side < 0:
            raise ValueError("Side must be > 0")
        super().__init__(side, side)


if __name__ == '__main__':
    r1 = Rectangle(3,2)
    r2 = Rectangle(1)
    print(r1.area)
    s1 = Square(3)
    print(s1.area)