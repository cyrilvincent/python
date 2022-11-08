from datetime import date
from dataclasses import dataclass
from typing import List


class Publisher:

    def __init__(self, name, address):
        self.name = name
        self.address = address

@dataclass()
class Author:

    first_name:str
    last_name: str
    id: int

class Book:

    vat = 0.05

    def __init__(self, title: str, id: int, price: float, publisher: Publisher, date: date = date(2022,11,8), category:int = 0, lang:str="fr-FR", authors:List[Author]=[]):
        self.title = title
        self.id = id
        self._price = price
        self.date = date
        self.category = category
        self.lang = lang
        self.publisher = publisher
        self.authors = authors

    def net_price(self):
        return self._price * (1 + Book.vat)

if __name__ == '__main__':
    p1 = Publisher("E2V", "St Egreve")
    a1 = Author("Cyril", "Vincent")
    b1 = Book("Python",123,20.99, p1, date(2022, 11, 8))
    print(b1)
    print(b1.title)
    b2 = Book("Python 3",123,25, p1, date(2022, 11, 8), authors=[a1])
    b1._price += 1
    b1.net_price()
    Book.net_price(b1)
    Book.vat = 0.055
