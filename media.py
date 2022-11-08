from datetime import date

class Publisher:

    pass

class Author:
    pass

class Book:

    vat = 0.05

    def __init__(self, title: str, id: int, price: float, date: date = date(2022,11,8), category:int = 0, lang:str="fr-FR"):
        self.title = title
        self.id = id
        self._price = price
        self.date = date
        self.category = category
        self.lang = lang

    def net_price(self):
        return self._price * (1 + Book.vat)

if __name__ == '__main__':
    b1 = Book("Python",123,20.99, date(2022, 11, 8))
    print(b1)
    print(b1.title)
    b2 = Book("Python 3",123,25, date(2022, 11, 8))
    b1._price += 1
    b1.net_price()
    Book.net_price(b1)
    Book.vat = 0.055
