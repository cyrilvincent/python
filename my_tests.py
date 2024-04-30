import unittest
import media

class MediaTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, 1+1)

    def test_media_net_price(self):
        b = media.Book("", 10)
        self.assertAlmostEquals(10.55, b.net_price, delta=1e-3)

    def test_media_cd(self):
        cd = media.Cd("", 10)
        self.assertAlmostEquals(12, cd.net_price, delta=1e-3)

    def test_media_robustness(self):
        with self.assertRaises(TypeError):
            m = media.Media("",0)
        cd = media.Cd("", 10)

    def test_cart(self):
        cart = media.Cart()
        cd = media.Cd("", 10)
        cart.add(cd)
        cart.add(media.Book("Python", 10))
        self.assertAlmostEqual(22.032, cart.total_net_price, delta=1e-2)

    def test_media_isbn(self):
        with self.assertRaises(ValueError):
            b = media.Book("",1,isbn="123")
        b = media.Book("",1, isbn="ISBN 978-2-7177-2113-4")
        self.assertEqual("ISBN 978-2-7177-2113-4", b.isbn)
        # try:
        #     b = media.Book("", 1, isbn="123")
        # except ValueError as ex:
        #     print(ex)


