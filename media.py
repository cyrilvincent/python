from dataclasses import dataclass
from typing import Optional, List
import abc
import re


@dataclass
class Author:

    first_name: str
    last_name: str

@dataclass
class Publisher:

    id: int
    name: str


class Media(metaclass=abc.ABCMeta):

    nb_media = 0
    vat = 0.2

    def __init__(self, title: str, price: float, weight_g: int=0, summary: str="", format: str="A3",
                 publisher: Optional[Publisher]=None, authors: List[Author]=[]):
        self.title = title
        self.price = price
        self.summary = summary
        self.format = format
        self.weight_g = weight_g
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @abc.abstractmethod
    def net_price(self):...

    def __repr__(self):
        return f"{type(self).__name__} {self.title} {self.price}"

    def __del__(self):
        Media.nb_media -= 1


class Book(Media):

    vat = 0.055

    def __init__(self, title: str, price: float, weight_g: int = 0, summary: str = "", format: str = "A3",
                 publisher: Optional[Publisher] = None, authors: List[Author] = [], nb_page=0, isbn: Optional[str]=None):
        super().__init__(title,price,weight_g,summary,format,publisher,authors)
        self.nb_page = nb_page
        self.regex = r"^(ISBN )?\d{3}-\d-\d{4}-\d{4}-\d$"
        self.regex_compile = re.compile(self.regex)
        self._isbn = None
        self.isbn = isbn


    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if value is not None and not re.match(self.regex_compile, value):
            raise ValueError("Bad ISBN")
        self._isbn = value


    # ajouter l'attribut isbn
    # tester le format isbn13

    @property
    def net_price(self):
        return self.price * (1 + Book.vat) * 0.95 + 0.01


class Cd(Media):

    def __init__(self, title: str, price: float, weight_g: int = 0, summary: str = "", format: str = "A3",
                 publisher: Optional[Publisher] = None, authors: List[Author] = [], nb_track=0):
        super().__init__(title, price, weight_g, summary, format, publisher, authors)
        self.nb_track = nb_track

    @property
    def net_price(self):
        return self.price * (1 + Media.vat)

# Créer Cd nb_track
# Créer Dvd zone

class Cart:

    def __init__(self):
        self.items: List[Media] = []

    def add(self, media: Media):
        self.items.append(media)

    def remove(self, media: Media):
        self.items.remove(media)

    @property
    def total_net_price(self):
        return sum([m.net_price for m in self.items])


if __name__ == '__main__':
    b1 = Book("Python", 10.0)
    print(b1.net_price)
    p1 = Publisher(0, "Cyril")
    b2 = Book("Python3", 15, publisher=p1)
    a1 = Author("Victor", "Hugo")
    b2.authors.append(a1)
    b2.authors = [a1]
    print(Media.nb_media)
    del b1
    print(Media.nb_media)



# Créer la classe Author avec @dataclass
# Idem pour publisher
# Créer la relation Book possède 0 ou 1 publisher
# Créer la relation Book possède n authors
# Tester
# Compter automatiquement le nombre de book créé : nb_book
# Mettre la TVA en static

# Cart
# items: List[Media]=[]
# add, remove
# total_net_price
