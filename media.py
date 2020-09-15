class Book:

    def __init__(self, title, price, publisher=None, category=None, format="A5"):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.category = category
        self.format = format

    def getNetPrice(self):
        return self.price * 1.055

if __name__ == '__main__':
    b1 = Book("Python pour les nuls",10)
    print(b1.getNetPrice())
