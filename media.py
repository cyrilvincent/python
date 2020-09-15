class Publisher:
    pass

class Cart:
    pass

class Book:

    nb = 0

    def __init__(self, title, price, authors = [], publisher=None, category=None, format="A5"):
        self.title = title
        self.price = price
        self.authors = authors
        self.publisher = publisher
        self.category = category
        self.format = format
        Book.nb += 1

    def getNetPrice(self):
        return self.price * 1.055

    def __del__(self):
        Book.nb -= 1

if __name__ == '__main__':
    b1 = Book("Python pour les nuls",10,["Cyril Vincent"])
    b1.authors.append("Toto")
    print(b1.getNetPrice())
    print(b1.authors)
    print(Book.nb)
    b2 = Book("Python pour les nuls",10,["Cyril Vincent"])
    print(Book.nb)
    del(b1)
    print(Book.nb)

