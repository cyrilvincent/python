class Rectangle:

    def __init__(self, length: float, width: float):
        # QUOI
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    # Instanciation
    r1 = Rectangle(3,2)
    print(r1.length, r1.width)
    r2 = Rectangle(length=3, width=4)
    print(r2.length, r2.width)
    print(r2.area())
    print(r2.perimeter())
    r2.area() # <=>
    Rectangle.area(r2) # Très peu utilisé