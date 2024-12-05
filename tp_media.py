# Class Publisher
# name, mail, phone
# Lier Book à Publisher et tester
# Class Author
# first_name, last_name, phone
# Lier Book à Authors et tester

class Book:

    def __init__(self, title, price, year, lang, nb_page=0):
        self.title = title
        self.price = price
        self.year = year
        self.nb_page = nb_page
        self.lang = lang

    def net_price(self):
        return self.price * 1.055


if __name__ == '__main__':
    b1 = Book("Les misérables", 10, 1862, "fr-FR")
    print(f"Book {b1.title} {b1.net_price():.2f}€")

