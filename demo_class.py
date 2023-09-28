class Book:

    # variables = attributs
    # fonctions = méthodes
    # fonction __init__ = constructeur
    # QUOI? COMMENT?

    def __init__(self, title, price, category="Computer", authors=[]):
        self.title = title
        self.price = price
        self.category = category
        self.authors = authors

    def get_net_price(self):
        return self.price * 1.055

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