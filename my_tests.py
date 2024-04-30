import unittest
import media

class MediaTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, 1+1)

    def test_media_net_price(self):
        b = media.Book("", 10)
        self.assertAlmostEquals(10.55, b.net_price, delta=1e-3)

    