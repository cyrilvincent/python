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

class Book:

    def __init__(self, title: str, price: float, year: int,publisher: Publisher, authors:list[Author]=[], nb_page: int=0) -> None:
        self.title = title
        self.price = price
        self.year = year
        self.publisher = publisher
        self.authors = authors
        self.nb_page = nb_page

    def net_price(self):
        return self.price * 1.055
    
if __name__=='__main__':
    a1 = Author("Cyril", "Vincent")
    p1 = Publisher("CEA")
    b1 = Book("Python pour les nuls", 10,2020,p1,[a1])
    print(b1.net_price())