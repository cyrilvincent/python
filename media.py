class Publisher:

    def __init__(self, name):
        self.name = name

class Media:

    def __init__(self, title, price, id, weight=0, publisher = None):
        self.title = title
        self.price = price
        self.weight = weight
        self.id = id
        Book.nbBook += 1
        self.publisher = publisher

    def netPrice(self):
        return self.price * 1.2

class Book(Media):

    nbBook = 0

    def __init__(self, title, price, id, weight=0, publisher = None, nbPage = 0):
        super().__init__(title, price,id,weight,publisher)
        Book.nbBook += 1
        self.nbPage = nbPage

    def netPrice(self):
        return self.price * 1.05

    def __del__(self):
        Book.nbBook -= 1

class Cd(Media):

    def __init__(self, title, price, id, weight=0, publisher = None, nbTrack = 0):
        super().__init__(title, price,id,weight,publisher)
        self.nbTrack = nbTrack

if __name__ == '__main__':

    b1 = Book("Python", 10.0, 1, publisher=Publisher("ENI"))
    print(b1.netPrice())
    print(b1.publisher.name)

    b2 = Book("",0,0)
    print(Book.nbBook)
    c = b2
    print(Book.nbBook)

    cd = Cd("Johnny",10,2)
    print(cd.netPrice())



