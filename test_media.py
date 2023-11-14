import unittest
from media import Cart, Media, Book, Cd

class MyTests(unittest.TestCase):

    def test_book_net_price(self):
        b1 = Book("0","Python",10)
        self.assertAlmostEqual(10.03, b1.net_price(), delta=0.01)

    def test_cart(self):
        cart = Cart()
        b1 = Book("0", "Python", 10)
        cart.add(b1)
        cd1 = Cd("0", "Celine Dion", 20)
        cart.add(cd1)
        self.assertAlmostEqual(34.03, cart.total_net_price, delta=0.1)


