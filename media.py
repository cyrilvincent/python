import datetime

# Gérer la TVA en attribut statique
# Vérifier qui si vous modifier la TVA tous les livres ont un TVA modifiée
# Trouver le moyen de compter les livres le plus simplement possible (nbBook)

class Book:

    def __init__(self, isbn, title, price, authors=[], publisher="", weight=-1, date=datetime.datetime.now(), nbpage=0 ):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.authors = authors
        self.publisher = publisher
        self.weight = weight
        self.date = date
        self.nbpage = nbpage

    def net_price(self):
        return self.price * (1 + 0.055)

    def toto(self, a, b):
        pass

if __name__ == '__main__':
    b1 = Book("007", "Python", 10.0)

    print(f"Le prix est: {b1.net_price():.2f} €")
    print(b1)
    b2 = Book("008", "Numpy", 19.99, authors=["Cyril"], date=datetime.datetime(2021,5,19,9,19))
    b2.price *= 1.1
    b2.toto(1,2)
    # <=>
    Book.toto(b2, 1, 2)