from typing import List


class Publisher:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Author:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Media:

    nb_media = 0

    def __init__(self, id: str, title: str, price: float, lang="fr-FR", rating=0, publisher: Publisher=None, authors: List[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.lang = lang
        self.rating = rating
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    def net_price(self):
        return self.price * 1.055

    def __del__(self):
        Media.nb_media -= 1

class Book(Media):

    def __init__(self, id: str, title: str, price: float, lang="fr-FR", rating=0, publisher: Publisher = None,
                 authors: List[Author] = [], nb_page=0):
        super().__init__(id, title,price,lang,rating,publisher,authors)
        self._nb_page = nb_page

    @property
    def nb_page(self):
        return self._nb_page

    @nb_page.setter
    def nb_page(self, value):
        self._nb_page = value

class Cd(Media):

    def __init__(self, id: str, title: str, price: float, lang="fr-FR", rating=0, publisher: Publisher = None,
                 authors: List[Author] = [], nb_track=0):

        super().__init__(id,title,price,lang,rating,publisher,authors)
        self.nb_tack = nb_track

if __name__ == '__main__':
    authors = [Author("1", "Cyril", "Vincent")]
    b1 = Book("001","Python",10, publisher=Publisher("0", "ATP"), authors = authors)
    print(b1.publisher.name)
    print(b1.authors[0].first_name)
    assert b1.net_price() == 10*1.055
    assert Media.nb_media == 1
    b2 = Book("002","Numpy", 20)
    assert Media.nb_media == 2
    del(b2)
    assert Media.nb_media == 1

# Créer la classe Publisher (id, name)
# Book -1 Publisher
# Créer la class Author (id, first_name, last_name, ...)
# Book -* Author