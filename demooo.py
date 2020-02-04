import abc

class Media(metaclass=abc.ABCMeta):

    def __init__(self, title, price):
        self.title = title
        self.price = price

    @abc.abstractmethod
    def netPrice(self):...


class Cd(Media):

    def __init__(self, title, price, nbTrack=0):
        super().__init__(title, price)
        self.nbTrack = nbTrack

    def netPrice(self):
        return self.price * 1.2

class Book(Media):

    nb = 0

    def __init__(self, title, price, nbPage=0):
        super().__init__(title, price)
        self.nbPage = nbPage
        Book.nb += 1


    def netPrice(self):
        return self.price * 1.055 * 0.95 + 0.01

    def __del__(self):
        Book.nb -= 1



book1 = Book("Python",10)
print(type(book1))
print(book1.title)
print(book1.price)
print(Book.nb)
book2 = Book("Numpy",20)
print(Book.nb)
cd1 = Cd("Johnny", 9)
# book1 = book2
# book1 = None
# del book1