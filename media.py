# class Publisher (id, name)
# Book possède 1 Publisher
# class Author (first_name, last_name)
# Book possède n Authors (list[Author])

# Media (tous les attributs sauf nb_page)
# Book (nb_page)
# Cd (nb_track)
# Dvd (zone)

class Author:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Publisher:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name



class Book:

    tva = 0.055

    def __init__(self, title: str, price: float, publisher: Publisher, authors: list[Author]=[], lang="fr-FR", note=0.0, nb_page=0):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.authors = authors
        self.lang = lang
        self.note = note
        self.nb_page = nb_page

    def get_net_price(self):
        return self.price * (1 + Book.tva)


if __name__ == '__main__':
    p1 = Publisher("001", "CEA")
    b1 = Book("Python", 10, p1)
    print(f"Prix du livre {b1.title}: {b1.get_net_price():.2f}€")
    b2 = Book("Python 3", 15, Publisher("002", "Leti"))
    print(f"Livre {b2.title} de l'éditeur {b2.publisher.name}")
    b3 = Book("Numpy", 20, p1, [Author("Cyril", "Vincent")])
    print(f"Livre {b3.title} de l'éditeur {b3.publisher.name} de l'auteur {b3.authors[0].last_name}")
