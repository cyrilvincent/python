class Rectangle:

    def __init__(self, long: float, larg: float):
        self.long = long
        self.larg = larg

    @property
    def surface(self):
        return self.long * self.larg

    @property
    def perimetre(self):
        return 2 * (self.long + self.larg)


if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.surface, r1.perimetre)
    # print(Rectangle.surface(r1))
    # r1.perimetre