import datetime

# Gérer la TVA en attribut statique
# Vérifier qui si vous modifier la TVA tous les livres ont un TVA modifiée
# Trouver le moyen de compter les livres le plus simplement possible (nbBook)

# Créer la classe Publisher (id, name, phone, mail, ...)
# Créer la relation un Book possède 1 publisher
# Créer un Cart possède * Books, add, remove, get_total_net_price

class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, isbn, title, price, authors=[], publisher="", weight=-1, date=datetime.datetime.now(), nbpage=0 ):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.authors = authors
        self.publisher = publisher
        self.weight = weight
        self.date = date
        self.nbpage = nbpage
        Book.nb_book += 1

    def net_price(self):
        return self.price * (1 + Book.tva)

    def toto(self, a, b):
        pass

    def __del__(self):
        Book.nb_book -= 1

if __name__ == '__main__':
    b1 = Book("007", "Python", 10.0)

    print(f"Le prix est: {b1.net_price():.2f} €")
    print(b1)
    b2 = Book("008", "Numpy", 19.99, authors=["Cyril"], date=datetime.datetime(2021,5,19,9,19))
    b2.price *= 1.1
    b2.toto(1,2)
    # <=>
    Book.toto(b2, 1, 2)
    Book.tva = 0.06
    print(b1.net_price())
    print(Book.nb_book)

    # Destruction
    # En ne faisant rien
    # En l'écrasant
    b1 = b2
    # En lui affactant None
    b1 = None
    # del immédiat
    # del(b1)
    print(Book.nb_book)
    del(b2)
    print(Book.nb_book)
