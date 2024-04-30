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

    def testu_cart(self):
        cart = media.Cart()
        cd = media.Cd("", 10)
        cart.add(cd)
        cart.add(media.Book("Python", 10))
        self.assertAlmostEquals(22.55, cart.total_net_price)


