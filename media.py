from datetime import datetime
from typing import List
import config


class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, title: str, price: float, lang: str="fr-FR", nb_page=0, date:datetime=datetime.now()):
        self.title = title
        self.price = price
        self.lang = lang
        self.date = date
        self._nb_page = nb_page
        Book.nb_book += 1

    def net_price(self):
        return self.price * (1 + Book.tva)

    def __del__(self):
        Book.nb_book -= 1

if __name__ == '__main__':
    print(config.copyright)
    b1 = Book("Python",10)
    print(f"Price: {b1.net_price():.2f}")
    print(b1._nb_page)
    print(b1.nb_book)
    b2 = Book("Python 3", 20)
    print(Book.nb_book)
    del(b1)
    print(Book.nb_book)

# TP
# Mettre la TVA en variable statique
# Compter automatiquement le nb de livre