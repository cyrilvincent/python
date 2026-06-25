class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    

if __name__ == "__main__":
    r1 = Rectangle(2,3)
    assert 6 == r1.area()
    assert 10 == r1.perimeter()