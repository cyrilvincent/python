class Publisher:
    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone

class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def get_nb_item(self):
        return len(self.items)

    def get_total_net_price(self):
        total = 0
        for item in self.items:
            total += item.get_net_price()
        return total

class Media:

    def __init__(self, title, price, authors = [], publisher=None, category=None):
        self.title = title
        self.price = price
        self.authors = authors
        self.publisher = publisher
        self.category = category

    def get_net_price(self):
        return self.price * 1.2

class Book(Media):
    nb = 0

    def __init__(self, title, price, authors=[], publisher=None, category=None, nbpage = 0):
        super().__init__(title,price,authors,publisher,category)
        self.nbpage = nbpage
        Book.nb += 1

    def __del__(self):
        Book.nb -= 1

    def get_net_price(self):
        return self.price * 1.055

class Cd(Media):

    def __init__(self, title, price, authors=[], publisher=None, category=None, nbtrack = 0):
        super().__init__(title,price,authors,publisher,category)
        self.nbtrack = nbtrack

class Dvd(Media):

    def __init__(self, title, price, authors=[], publisher=None, category=None, zone = 0):
        super().__init__(title,price,authors,publisher,category)
        self.zone = zone



if __name__ == '__main__':
    p1 = Publisher("ENI")
    b1 = Book("Python pour les nuls",10,["Cyril Vincent"],p1)
    b1.authors.append("Toto")
    print(b1.get_net_price())
    print(b1.authors)
    print(Book.nb)
    b2 = Book("Python pour les nuls",10,["Cyril Vincent"])
    print(Book.nb)
    #del(b1)
    print(Book.nb)
    cart = Cart()
    cart.add(b1)
    cart.add(b2)
    cd = Cd("Allumer le feu",10,["Jojo"],nbtrack=10)
    cart.add(cd)
    dvd = Dvd("La reine des neiges",20,["Disney"],zone=3)
    cart.add(dvd)
    print(cart.get_nb_item())
    print(cart.get_total_net_price())


