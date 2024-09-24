class Rectangle:

    def __init__(self, length: float, width: float):
        # QUOI
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return  2 * (self.length + self.width)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.get_area())
    print(r1.get_perimeter())