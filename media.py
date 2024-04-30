from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Author:

    first_name: str
    last_name: str

@dataclass
class Publisher:

    id: int
    name: str


class Book:

    nb_book = 0
    vat = 0.055

    def __init__(self, title: str, price: float, weight_g: int=0, nb_page: int=0, summary: str="", format: str="A3",
                 publisher: Optional[Publisher]=None, authors: List[Author]=[]):
        self.title = title
        self.price = price
        self.nb_page = nb_page
        self.summary = summary
        self.format = format
        self.weight_g = weight_g
        self.publisher = publisher
        self.authors = authors
        Book.nb_book += 1

    @property
    def net_price(self):
        return self.price * (1 + Book.vat)

    def __repr__(self):
        return f"Book {self.title} {self.price}"

    def __del__(self):
        Book.nb_book -= 1

# Créer Cd nb_track
# Créer Dvd zone


if __name__ == '__main__':
    b1 = Book("Python", 10.0)
    print(b1.net_price)
    p1 = Publisher(0, "Cyril")
    b2 = Book("Python3", 15, publisher=p1)
    a1 = Author("Victor", "Hugo")
    b2.authors.append(a1)
    b2.authors = [a1]
    print(Book.nb_book)
    del b1
    print(Book.nb_book)



# Créer la classe Author avec @dataclass
# Idem pour publisher
# Créer la relation Book possède 0 ou 1 publisher
# Créer la relation Book possède n authors
# Tester
# Compter automatiquement le nombre de book créé : nb_book
# Mettre la TVA en static
