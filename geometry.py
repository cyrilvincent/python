class Rectangle:

    def __init__(self, length: float, width: float):
        """
        Rectangle
        :param length:
        :param width:
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Aire du rectangle
        :return:
        """
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    r1 = Rectangle(2,3)
    print(r1)
    assert r1.area() == 6
    assert r1.perimeter() == 10
    Rectangle.area(r1) # <=> r1.area()
    r2 = Rectangle(4,3)
    r2.length += 1
