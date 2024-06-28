class Rectangle:

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
if __name__=='__main__':
    r1 = Rectangle(3,2)
    print(r1.area(), r1.perimeter())
    r2 = Rectangle(4,1)
    # Rectangle.area(r2)