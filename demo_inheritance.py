class Point:

    def __init__(self,x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, length, width, coord):
        self.length = length
        self.width = width
        self.coord = coord # Association (HAS)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle): # Inheritance (IS)

    def __init__(self, side, coord):
        super().__init__(length=side, width=side, coord=coord)



if __name__ == '__main__':
    x1 = Point(2,3)
    r1 = Rectangle(4,5, x1)
    print(r1.area(), r1.perimeter())
    s1 = Square(3, x1)
    print(s1.area(), s1.perimeter())