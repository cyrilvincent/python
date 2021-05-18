class Rectangle:
    # QUOI => attributs => variables
    # COMMENT => méthodes
    # ETANCHEITE de l'objet

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self): # Méthode
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    monrectangle = Rectangle(width=2)
    # monrectangle = instance ou l'objet
    # Rectangle = classe
    # () = instanciation, permet de créer une instance à partir d'une classe
    r1 = Rectangle(4,3)
    r2 = Rectangle(1)
    print(r1.length, r1.width)
    print(r1.area(), r1.perimeter())