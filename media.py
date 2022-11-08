class Book:

    def __init__(self, title: str, id: int, price: float):
        self.title = title
        self.id = id
        self.price = price

if __name__ == '__main__':
    b1 = Book("Python",123,20.99)
    print(b1)
    print(b1.title)
