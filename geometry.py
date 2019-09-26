class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, length, width, origin:Point = Point(0,0)):
        self._length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self._length * self.width

    def perimeter(self):
        return 2 * (self.width + self._length)

    def __repr__(self):
        return f"Rectangle({self._length},{self.width})"

    def __eq__(self, other):
        return self._length == other._length and self.width == other.width

    def __ne__(self, other):
        return self._length != other._length or self.width != other.width


    def __add__(self, other):
        return Rectangle(self._length + other._length, self.width + other.width)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    #r1._length = 2
    print(r1)
    print(r1.area())
    print(r1.perimeter())

    r1.origin.move(5,5)




    r2 = Rectangle(3,2)
    print(r1 == r2)
    print(r1 is r2)

    r3 = r1 + r2
    print(r3)

    l1 = [1,2,3]
    l2 = [1,2,3]
    print(l1 == l2)
    print(l1 is l2)


    # r2 = r1
    # print(r1 == r2)
    # print(r1 is r2)

    def toto(self):
        return 0

    Rectangle.toto = toto

    print(r1.toto())


