# Concevoir la classe Book avec 5 à 10 attributs
# vat_price 5.5%
# class Cart
# items
# add, remove, clear
import numpy as np
import datetime

class Book:

    def __init__(self,
                 isbn: str,
                 title: str,
                 price: float,
                 authors: list,
                 publisher,
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

    def net_price(self):
        return self.price * 1.055


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def clear(self):
        self.items.clear()


if __name__ == '__main__':
    b1 = Book("978-2-07-061275-8", "Python pour les nuls", 10, ["Cyril"], "CEA", 99)
    assert np.round(b1.net_price(), 2) == 10.55
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
