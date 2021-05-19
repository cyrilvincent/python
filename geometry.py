class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_rel(self, x, y):
        self.x += x
        self.y += y


class Rectangle:
    # QUOI => attributs => variables
    # COMMENT => méthodes
    # ETANCHEITE de l'objet

    color = "black"

    def __init__(self, length=0, width=0, coord=Point()):
        self.length = length
        self.width = width
        self.coord = coord

    def area(self): # Méthode
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    monrectangle = Rectangle(width=2)
    # monrectangle = instance ou l'objet
    # Rectangle = classe
    # () = instanciation, permet de créer une instance à partir d'une classe
    p1 = Point(2,-4)
    r1 = Rectangle(4,3,p1)
    r2 = Rectangle(1)
    r2.coord = p1
    r2.coord = Point(2,-8)
    r2.coord.move_rel(1,1)
    print(r1.length, r1.width)
    print(r1.area(), r1.perimeter())
    Rectangle.color = "RED"
    print(Rectangle.color)