import abc

class Publisher:

    def __init__(self, name):
        self.name = name

class Media(metaclass=abc.ABCMeta):

    def __init__(self, id, title, price, publisher:Publisher):
        self.id = id
        self.title = title
        self.price = price
        self.publisher = publisher

    @abc.abstractmethod
    def getNetPrice(self):...

    def __repr__(self):
        return f"{type(self).__name__}: {self.id} {self.title}"

class Book(Media):

    def __init__(self, id, title, price, publisher: Publisher, nbPage = 0):
        super().__init__(id,title,price,publisher)
        self.nbPage = nbPage

    def getNetPrice(self):
        return self.price * 1.05 * 0.95 + 0.01



class Cart:

    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def getTotalNetPrice(self):
        return sum([i.getNetPrice() for i in self._items])

if __name__ == '__main__':
    p1 = Publisher("ENI")
    b1 = Book(1,"Python",22.3,p1)
    print(b1)
    b2 = Book(2,"Numpy",3.65,p1)
    cart = Cart()
    cart.add(b1)
    cart.add(b2)
    print(cart.getTotalNetPrice())
    print(cart._items)

