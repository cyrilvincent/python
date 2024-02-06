from datetime import datetime
from typing import List
import config


class Book:

    def __init__(self, title: str, price: float, lang: str="fr-FR", nb_page=0, date:datetime=datetime.now()):
        self.title = title
        self.price = price
        self.lang = lang
        self.date = date
        self._nb_page = nb_page

    def net_price(self):
        return self.price * 1.055

    def __del__(self):
        pass
        # del(b1)
        # b1 = None
        # b1 = x
        # sortir du bloc

if __name__ == '__main__':
    print(config.copyright)
    b1 = Book("Python",10)
    print(f"Price: {b1.net_price():.2f}")
    print(b1._nb_page)

# TP
# Mettre la TVA en variable statique
# Compter automatiquement le nb de livre