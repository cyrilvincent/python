# Class Publisher
# name, mail, phone
# Lier Book à Publisher et tester
# Class Author
# first_name, last_name, phone
# Lier Book à Authors et tester
class Publisher:

    def __init__(self, name, mail, phone):
        self.name = name
        self.mail = mail
        self.phone = phone

class Author:

    def __init__(self, first_name, last_name, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone


class Book:

    def __init__(self, title, price, year, lang, publisher: Publisher, authors: list[Author], nb_page=0):
        self.title = title
        self.price = price
        self.year = year
        self.nb_page = nb_page
        self.lang = lang
        self.publisher = publisher
        self.authors = authors

    def net_price(self):
        return self.price * 1.055


if __name__ == '__main__':
    p1 = Publisher("Lacroix", "contact@lacroix.com", "0612345678")
    a1 = Author("Victor", "Hugo")
    b1 = Book("Les misérables", 10, 1862, "fr-FR", p1, [a1])
    print(f"Book {b1.title} {b1.net_price():.2f}€")
    print(b1.publisher.name)

