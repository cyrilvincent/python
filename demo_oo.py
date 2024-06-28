class Coord:

    def __init__(self, x: float=0, y: float=0) -> None:
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, length: float, width: float, coord: Coord = Coord()) -> None:
        self.length = length
        self.width = width
        self.coord = coord

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Square(Rectangle):

    def __init__(self, side: float, coord: Coord = Coord()) -> None:
        super().__init__(side, side, coord)
    
    
class VideoGame:

    def __init__(self, rectangles: list[Rectangle]=[]) -> None:
        self.rectangles = rectangles

    def score(self):
        return sum([r.area() for r in self.rectangles])
    
if __name__=='__main__':
    c1 = Coord(-1, 1)
    r1 = Rectangle(3,2, c1)
    print(r1.area(), r1.perimeter())
    r2 = Rectangle(4,1, Coord(1,2))
    # Rectangle.area(r2)
    r2.coord.move(3,2)
    r2.coord.x = 4
    c00 = Coord()
    vg = VideoGame([r1, r2])
    s1 = Square(3)
    print(s1.area())
