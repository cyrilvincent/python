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



class Media:

    tva = 0.2
    nb_media = 0

    def __init__(self, title: str, price: float,publisher: Publisher=None, lang: str="fr-FR", date:datetime=datetime.now(), authors: List[Author]=[] ):
        self.title = title
        self.price = price
        self.lang = lang
        self.date = date
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    def net_price(self):
        return self.price * (1 + Media.tva)

    def __del__(self):
        Media.nb_media -= 1

class Book(Media):

    tva = 0.055

    def __init__(self, title: str, price: float, publisher: Publisher = None, lang: str = "fr-FR",
                 date: datetime = datetime.now(), authors: List[Author] = [], nb_page=0):
        super().__init__(title, price,publisher,lang,date,authors)
        self.nb_page = nb_page

    def net_price(self):
        return self.price * 0.95 * (1 + Book.tva) + 0.01

class Cd(Media):

    def __init__(self, title: str, price: float, publisher: Publisher = None, lang: str = "fr-FR",
                 date: datetime = datetime.now(), authors: List[Author] = [], nb_track=0):
        super().__init__(title, price,publisher,lang,date,authors)
        self.nb_track = nb_track

class Cart:

    def __init__(self):
        self.medias: List[Media] = []

    def add(self, m: Media):
        self.medias.append(m)

    def remove(self, m:Media):
        self.medias.remove(m)

    def total_net_price(self):
        res = 0
        for media in self.medias:
            res += media.net_price()
        return res

if __name__ == '__main__':
    print(config.copyright)
    p1 = Publisher("Python.org", "0123456789", "a@a.a")
    a1 = Author("Cyril", "Vincent")
    b1 = Book("Python",10,publisher=p1, authors=[a1])
    print(f"Price: {b1.net_price():.2f}")
    print(b1.nb_media)
    b2 = Book("Python 3", 20)
    print(Book.nb_media)
    del(b1)
    print(Book.nb_media)
    b2.authors.append(a1)
    b2.authors = [Author("Cyril", "Vincent"), Author("toto", "titi")]
    cd = Cd("Allumer le feu",10)



# TP
# Mettre la TVA en variable statique
# Compter automatiquement le nb de livre