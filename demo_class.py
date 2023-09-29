# Créer la classe Publisher et Author PlusieurMot
# Pas de méthode
# Tester et vérifier le type

class Publisher:

    def __init__(self, name, address, mail):
        self.name = name
        self.address = address
        self.mail = mail

class Author:

    def __init__(self, first_name, last_name, mail=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail

class Book:

    # variables = attributs
    # fonctions = méthodes
    # fonction __init__ = constructeur
    # QUOI? COMMENT?

    nb_book = 0

    def __init__(self, title, price, category="Computer", authors=[]):
        self.title = title
        self.price = price
        self.category = category
        self.authors = authors
        Book.nb_book += 1

    def get_net_price(self):
        return self.price * 1.055

    def __del__(self):
        Book.nb_book -= 1


if __name__ == '__main__':
    b1 = Book("Python", 10)
    print(b1.title)
    print(b1.get_net_price())
    b2 = Book("Qt", price=20)
    b2.price += 1
    print(b2.get_net_price())
    b3 = Book("Python", 10)
    print(b1 == b3)
    print(b1.price == b3.price and b1.title == b3.title)
    a1 = Author("Victor", "Hugo")
    a2 = Author("Cyril", "Vincent", "contact@cyrilvincent.com")
    p1 = Publisher("ENI", "inconnue", "contact@eni.fr")
    print(b1.nb_book)
    del b3
    print(b1.nb_book)