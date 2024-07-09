import unittest
import geometry
import media

class MyTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(2, 1+1)

    def test_square_area(self):
        s = geometry.Square(3)
        self.assertEqual(9, s.area)

    def test_squere_side_negative_robustness(self):
        with self.assertRaises(ValueError):
            s = geometry.Square(-1)

    def test_book_net_price(self):
        b = media.Book(1,"",10)
        self.assertAlmostEqual(10.55, b.net_price, delta=1e-3)

    def test_abc(self):
        # p = geometry.Polygon()
        r = geometry.Rectangle(3,2)


