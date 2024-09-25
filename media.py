# class Publisher (id, name)
# Book possède 1 Publisher
# class Author (first_name, last_name)
# Book possède n Authors (list[Author])

class Book:

    tva = 0.055

    def __init__(self, title: str, price: float, lang="fr-FR", note=0.0, nb_page=0):
        self.title = title
        self.price = price
        self.lang = lang
        self.note = note
        self.nb_page = nb_page

    def get_net_price(self):
        return self.price * (1 + Book.tva)

if __name__ == '__main__':
    b1 = Book("Python", 10)
    print(f"Prix du livre {b1.title}: {b1.get_net_price():.2f}€")

