from datetime import datetime
from typing import List
import config


# class Publisher (name, phone, mail)
# class Author (first_name, last_name)
# Book -1 Publisher
# Book -* Author

class Publisher:

    def __init__(self, name: str, phone: str, mail: str):
        self.name = name
        self.phone = phone
        self.mail = mail

class Author:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname



class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, title: str, price: float,publisher: Publisher=None, lang: str="fr-FR", nb_page=0, date:datetime=datetime.now(), authors: List[Author]=[] ):
        self.title = title
        self.price = price
        self.lang = lang
        self.date = date
        self._nb_page = nb_page
        self.publisher = publisher
        self.authors = authors
        Book.nb_book += 1

    def net_price(self):
        return self.price * (1 + Book.tva)

    def __del__(self):
        Book.nb_book -= 1

if __name__ == '__main__':
    print(config.copyright)
    p1 = Publisher("Python.org", "0123456789", "a@a.a")
    a1 = Author("Cyril", "Vincent")
    b1 = Book("Python",10,publisher=p1, authors=[a1])
    print(f"Price: {b1.net_price():.2f}")
    print(b1._nb_page)
    print(b1.nb_book)
    b2 = Book("Python 3", 20)
    print(Book.nb_book)
    del(b1)
    print(Book.nb_book)
    b2.authors.append(a1)


# TP
# Mettre la TVA en variable statique
# Compter automatiquement le nb de livre