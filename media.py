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

    def __repr__(self):
        return f"{type(self).__name__}: {self.title} {self.price}"

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

    # def __getattribute__(self, item):
    #     if item == "title":
    #         return "X"
    #     else:
    #         return super().__getattribute__(item)

import sqlite3
class BookDb:

    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass

    def getBySql(self, sql):
        self.cursor.execute(sql)
        # for row in cursor:
        #     yield Book(row[1], row[2], row[0])
        return (Book(row[2], row[1], row[0]) for row in self.cursor)

    def getAll(self):
        return self.getBySql("select * from book")

    def getByPrice(self, price):
        return self.getBySql(f"select * from book where price <= {price}")

    def getByTitle(self, title):
        return self.getBySql(f"select * from book where upper(title) like '%{title.upper()}%'")

if __name__ == '__main__':

    db = BookDb("data/books.db3")
    print(list(db.getAll()))
    print(list(db.getByPrice(15)))
    print(list(db.getByTitle("py")))

    # b1 = Book("Python", 10.0, 1, publisher=Publisher("ENI"))
    # print(b1.netPrice())
    # print(b1.publisher.name)
    #
    # b2 = Book("",0,0)
    # print(Book.nbBook)
    # c = b2
    # print(Book.nbBook)
    #
    # cd = Cd("Johnny",10,2)
    # print(cd.netPrice())
    #
    # print(cd.title)
    #
    # print(cd.__dict__)
    # cd.__dict__["title"]+="X"
    # print(cd.title)
    #
    # l = [b1, b2,cd]
    # import jsonpickle
    # s = jsonpickle.encode(l,unpicklable=False)
    # with open("data/books.toto","w") as f:
    #     print(s)
    #     f.write(s)




