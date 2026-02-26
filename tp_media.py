# Concevoir la classe Book avec 5 à 10 attributs
# vat_price 5.5%
# class Cart
# items
# add, remove, clear
import numpy as np
import datetime

class Publisher:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

class Author:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class Book:

    # Gérer un TVA commune à tous les livres
    # Reprogrammer net_price
    # Compter automatiquement le nb de book

    vat = 0.055
    nb = 0

    def __init__(self,
                 isbn: str,
                 title: str,
                 price: float,
                 authors: list[Author],
                 publisher: Publisher,
                 nb_page=0,
                 date=datetime.date.today(),
                 lang="fr-FR",
                 ):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.authors = authors
        self.nb_page = nb_page
        self.publisher = publisher
        self.date = date
        self.lang = lang
        Book.nb += 1

    def net_price(self):
        return self.price * (1 + Book.vat)

    def __del__(self):
        Book.nb -= 1


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def clear(self):
        self.items.clear()


class Counter:

    i = 0

    def increment(self):
        Counter.i += 1


if __name__ == '__main__':
    pub = Publisher("007", "CEA")
    b1 = Book("978-2-07-061275-8", "Python pour les nuls", 10, [Author("Cyril", "Vincent")], pub, 99)
    # Book.nb
    assert np.round(b1.net_price(), 2) == 10.55
    b2 = Book("978-2-07-061275-9", "Python 3", 10, [Author("Cyril", "Vincent"), Author("toto", "titi")], pub, 99)
    assert Book.nb == 2
    del b2
    assert Book.nb == 1
    assert b1.publisher.name == "CEA"
    assert b1.authors[0].first_name == "Cyril"
    print(Book.nb)
    cart = Cart()
    cart.add("oignons")
    print(cart.items)
    cart.add("salade")
    print(cart.items)
    cart.add("salade")
    print(cart.items)
    cart.remove("salade")
    print(cart.items)
    cart.add(b1)
    print(cart.items)
    assert len(cart.items) == 3
    c1 = Counter()
    c1.increment()
    c1.increment()
    c2 = Counter()
    c2.increment()
    print(c1.i, c2.i)

# Book, Cd, Dvd
# Media
# Bonus : Item
