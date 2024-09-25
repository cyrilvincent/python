class Coord:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def move_relative(self, x: float, y: float):
        self.x += x
        self.y += y

class Rectangle:

    def __init__(self, length: float, width: float, coord: Coord):
        # QUOI
        self.length = length
        self.width = width
        self.coord = coord

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return  2 * (self.length + self.width)

if __name__ == '__main__':
    c1 = Coord(4,-1)
    r1 = Rectangle(3,2, c1)
    print(r1.get_area())
    print(r1.get_perimeter())
    r2 = Rectangle(2,4,Coord(5,2))
    r2.coord.move_relative(1,-2)
    print(f"Coordonnées ({r2.coord.x},{r2.coord.y})")