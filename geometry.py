class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def moveRel(self, x, y):
        self.x += x
        self.y += y


class Rectangle:

    nb = 0

    def __init__(self, width, length, origin = Point()):
        self.width = width
        self._length = length
        self.origin = origin
        Rectangle.nb += 1

    def __del__(self):
        Rectangle.nb -= 1

    def getPerimeter(self):
        return 2 * (self.width + self._length)

    def getArea(self):
        return self.width * self._length



if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.getPerimeter())
    print(r1.getArea())
    print(r1)
    r2 = Rectangle(3,2)
    print(r1 == r2)
    print(r2)
    r2 = r1
    print(r1)
    print(r2)
    print(r1 == r2)
    r1._length = 99
    print(r2._length)

    l1 = []
    l1.append(Rectangle(2,3))
    l1.append(Rectangle(4,3))

    r1 = Rectangle(4,3)
    l2=[]
    l2.append(r1)
    r1.width=5
    r1._length=6
    l2.append(r1)
    for r in l2:
        print(r.width, r._length)

    print(r1.getArea())
    print(Rectangle.getArea(r1))

    r3 = Rectangle(3,2,Point(4,6))
    r3.origin.moveTo(8,9)

