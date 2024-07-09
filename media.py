# Book
# 5 & 7 attributs
# 1 méthode net_price() = price * 1.055
from dataclasses import dataclass
import abc
from typing import Optional
# dataclass Publisher (name) + Author (first_name, last_name)
# 1 book possède 1 ou 0 publisher
# 1 book possède * authors
# nb_book static qui compte et décremente les book à la création destruction
# mettre la tva en static

# Media, Book (nb_page), cd (nb_track), Dvd (zone)
# Cart plusieurs Media
# total_net_price
# UT

@dataclass
class Publisher:

    name: str


@dataclass
class Author:

    first_name: str
    last_name: str


class Media(abc.ABC):

    nb_media = 0
    tva = 0.2

    def __init__(self,
                 id: int,
                 title: str,
                 price: float,
                 rate: int | None = None,
                 language: str = "fr-FR",
                 publisher: Publisher | None = None,
                 authors: list[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.rate = rate
        self.language = language
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @property
    def net_price(self):
        return self.price * (1 + Media.tva)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __del__(self):
        Media.nb_media -= 1


class Book(Media):

    def __init__(self,
                 id: int,
                 title: str,
                 price: float,
                 rate: int | None = None,
                 language: str = "fr-FR",
                 publisher: Publisher | None = None,
                 authors: list[Author] = [],
                 nb_page: int = 0):
        super().__init__(id, title, price, rate, language, publisher, authors)
        self.nb_page = nb_page

    @property
    def net_price(self):
        return self.price * 1.055


class Cd(Media):

    def __init__(self,
                 id: int,
                 title: str,
                 price: float,
                 rate: int | None = None,
                 language: str = "fr-FR",
                 publisher: Publisher | None = None,
                 authors: list[Author] = [],
                 nb_track: int = 0):
        super().__init__(id, title, price, rate, language, publisher, authors)
        self.nb_track = nb_track


class Cart:

    def __init__(self):
        self.medias = []


    @property
    def total_net_price(self):
        return sum([m.net_price if m.net_price is not None else 0 for m in self.medias])









if __name__ == '__main__':
    b1 = Book(1, "Python", 10)
    print(b1.net_price)
    # Book.net_price(b1)
    p = Publisher("Cyril")
    b2 = Book(1,"Numpy", 9, publisher=p, authors=[Author("Cyril", "Vincent")])
    print(b2.authors[0].first_name)

    b1.__dict__["toto"]= "titi"
    print(b1.__dict__)


