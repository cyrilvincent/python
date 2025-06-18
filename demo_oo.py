class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    assert 6 == r1.area()
    assert 10 == r1.perimeter()
    r2 = Rectangle(3,3)
    rectangles: list[Rectangle] = [r1, r2]
    for r in rectangles:
        print(r.area())
    print([r.area() + r.perimeter() for r in rectangles])
