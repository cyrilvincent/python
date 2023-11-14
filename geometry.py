class Rectangle:

    def __init__(self, length: float, width: float):
        """
        Rectangle
        :param length:
        :param width:
        """
        self._length = length
        self._width = width

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
    r1 = Rectangle(2,3)
    print(r1)
    assert r1.area == 6
    assert r1.perimeter() == 10
    # Rectangle.area(r1) # <=> r1.area()
    r2 = Rectangle(4,3)
    r2._length += 1
    r1 = None
    r1 = r2
    del(r1)
