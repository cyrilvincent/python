# class Book avec 5 à 10 attributs
# méthode net_price() = price * 1.055
# Un book possède un publisher (name)
# Un book possède n authors (first_name, last_name)
import datetime
from typing import Callable

class Author:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Publisher:

    def __init__(self, name: str) -> None:
        self.name = name

class Media:

    def __init__(self, title: str, price: float, year: int,publisher: Publisher, authors:list[Author]=[]) -> None:
        self.title = title
        self.price = price
        self.year = year
        self.publisher = publisher
        self.authors = authors

    def net_price(self):
        return self.price * 1.2
    
class Book(Media):

    def __init__(self, title: str, price: float, year: int,publisher: Publisher, authors:list[Author]=[], nb_page:int = 0) -> None:
        super().__init__(title, price,year,publisher, authors)
        self.nb_page = nb_page

    def net_price(self):
        return self.price * 1.055
    

class Cd(Media):

    def __init__(self, title: str, price: float, year: int,publisher: Publisher, authors:list[Author]=[], nb_track:int = 0) -> None:
        super().__init__(title, price,year,publisher, authors)
        self.nb_track = nb_track

class Cart:

    def __init__(self) -> None:
        self.items: list[Media] = []

    def add(self, m: Media):
        self.items.append(m)

    def remove(self, m: Media):
        self.items.remove(m)

    def total_net_price(self) -> float:
        return sum([m.net_price() for m in self.items])
    
if __name__=='__main__':
    a1 = Author("Cyril", "Vincent")
    p1 = Publisher("CEA")
    b1 = Book("Python pour les nuls", 10,2020,p1,[a1])
    print(b1.net_price())
    cd = Cd("Allumer le feu",10,2000,p1, [Author("Johnny", "Hallyday")])
    cart = Cart()
    cart.add(b1)
    cart.add(cd)
    print(cart.total_net_price())