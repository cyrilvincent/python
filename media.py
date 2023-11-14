class Book:

    nb_book = 0

    def __init__(self, id: str, title: str, price: float, nb_page=0, lang="fr-FR", rating=0):
        self.id = id
        self.title = title
        self.price = price
        self._nb_page = nb_page
        self.lang = lang
        self.rating = rating
        Book.nb_book += 1

    def net_price(self):
        return self.price * 1.055

    @property
    def nb_page(self):
        return self._nb_page

    @nb_page.setter
    def nb_page(self, value):
        self._nb_page = value

    def __del__(self):
        Book.nb_book -= 1


if __name__ == '__main__':
    b1 = Book("001","Python",10)
    assert b1.net_price() == 10*1.055
    assert Book.nb_book == 1
    b2 = Book("002","Numpy", 20)
    assert Book.nb_book == 2
    del(b2)
    assert Book.nb_book == 1

# Créer la classe Publisher (id, name)
# Book -1 Publisher
# Créer la class Author (id, first_name, last_name, ...)
# Book -* Author