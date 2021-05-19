import datetime


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


if __name__ == '__main__':
    b1 = Book("007", "Python", 10.0)
    print(f"Le prix est: {b1.net_price():.2f} €")