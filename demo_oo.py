class Rectangle:

    def __init__(self, length, width): # Constructeur
        self.length = length  # Attributs
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 *(self.width + self.length)

if __name__ == '__main__':
    r1 = Rectangle(3,2)
    print(r1.area())
    print(r1.perimeter())