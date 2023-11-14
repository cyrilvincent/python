class Book:

    def __init__(self, id: str, title: str, price: float, nb_page=0, lang="fr-FR", rating=0):
        self.id = id
        self.title = title
        self.price = price
        self.nb_page = nb_page
        self.lang = lang
        self.rating = rating

    def net_price(self):
        return self.price * 1.055


if __name__ == '__main__':
    b1 = Book("001","Python",10)
    assert b1.net_price() == 10*1.055

# Passe le nb_page en private + property
# Passe le net_price en property
# Compte automatiquement le nb_book