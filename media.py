# Book
# 5 & 7 attributs
# 1 méthode net_price() = price * 1.055
from dataclasses import dataclass
from typing import Optional
# dataclass Publisher (name) + Author (first_name, last_name)
# 1 book possède 1 ou 0 publisher
# 1 book possède * authors
# nb_book static qui compte et décremente les book à la création destruction
# mettre la tva en static

@dataclass
class Publisher:

    name: str


@dataclass
class Author:

    first_name: str
    last_name: str


class Book:

    nb_book = 0
    tva = 0.055

    def __init__(self,
                 id: int,
                 title: str,
                 price: float,
                 format: str="A3",
                 nb_page: int = 0,
                 rate: int | None = None,
                 language: str = "fr-FR",
                 publisher: Publisher | None = None,
                 authors: list[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.format = format
        self.nb_page = nb_page
        self.rate = rate
        self.language = language
        self.publisher = publisher
        self.authors = authors
        Book.nb_book += 1

    def net_price(self):
        return self.price * (1 + Book.tva)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __del__(self):
        Book.nb_book -= 1




if __name__ == '__main__':
    b1 = Book(1, "Python", 10)
    print(b1.net_price())
    Book.net_price(b1)
    p = Publisher("Cyril")
    b2 = Book(1,"Numpy", 9, publisher=p, authors=[Author("Cyril", "Vincent")])
    print(b2.authors[0].first_name)


