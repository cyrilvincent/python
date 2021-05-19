import datetime

# Gérer la TVA en attribut statique
# Vérifier qui si vous modifier la TVA tous les livres ont un TVA modifiée
# Trouver le moyen de compter les livres le plus simplement possible (nbBook)

# Créer la classe Publisher (id, name, phone, mail, ...)
# Créer la relation un Book possède 1 publisher
# Créer un Cart possède * Books, add, remove, get_total_net_price

class Publisher:

    def __init__(self, id, name, phone="", mail=""):
        self.id = id
        self.name = name
        self.phone = phone
        self.mail = mail


class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, isbn, title, price, authors=[], publisher=Publisher(0,""), weight=-1, date=datetime.datetime.now(), nbpage=0 ):
        self.publisher = publisher
        self.isbn = isbn
        self.title = title
        self.price = price
        self.authors = authors
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

class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def total_net_price(self):
        total = 0
        for item in self.items:
            total += item.net_price()
        return total

    def total_net_price_2(self):
        return sum([item.net_price() for item in self.items])

if __name__ == '__main__':
    p1 = Publisher(1, "ENI")
    b1 = Book("007", "Python", 10.0, publisher=p1)
    print(b1.publisher.name)
    print(f"Le prix est: {b1.net_price():.2f} €")
    print(b1)
    b2 = Book("008", "Numpy", 20, authors=["Cyril"], date=datetime.datetime(2021,5,19,9,19))

    b2.publisher = p1
    b2.price *= 1.1
    b2.toto(1,2)
    # <=>
    Book.toto(b2, 1, 2)
    Book.tva = 0.06
    print(b1.net_price())
    print(Book.nb_book)

    cart = Cart()
    print(f"Cart net price: {cart.total_net_price():.2f}")
    print(f"Cart net price 2: {cart.total_net_price_2():.2f}")
    cart.add(b1)
    print(f"Cart net price: {cart.total_net_price():.2f}")
    print(f"Cart net price 2: {cart.total_net_price_2():.2f}")
    cart.add(b2)
    print(f"Cart net price: {cart.total_net_price():.2f}")
    print(f"Cart net price 2: {cart.total_net_price_2():.2f}")
    print(cart.items[0].publisher.name)
    cart.remove(b2)
    print(f"Cart net price: {cart.total_net_price():.2f}")
    print(f"Cart net price 2: {cart.total_net_price_2():.2f}")
    cart.remove(b1)
    print(f"Cart net price: {cart.total_net_price():.2f}")
    print(f"Cart net price 2: {cart.total_net_price_2():.2f}")


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
