class Book:

    def __init__(self, title: str, price: float, weight_g: int=0, nb_page: int=0, summary: str="", format:str="A3"):
        self.title = title
        self.price = price
        self.nb_page = nb_page
        self.summary = summary
        self.format = format
        self.weight_g = weight_g

    @property
    def net_price(self):
        return self.price * 1.055

if __name__ == '__main__':
    b1 = Book("Python", 10.0)
    print(b1.net_price)
