import unittest
import geometry
import media
import services


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

    def test_cd(self):
        cd = media.Cd(1,"Allumer le feu", 10)
        self.assertAlmostEqual(12, cd.net_price, delta=1e-3)

    def test_cart(self):
        cart = media.Cart()
        b = media.Book(1, "", 10)
        cd = media.Cd(1, "Allumer le feu", 10)
        cart.medias.append(b)
        cart.medias.append(cd)
        self.assertAlmostEqual(22.55, cart.total_net_price, delta=1e-3)

    def test_db(self):
        s = services.CartService()
        res = s.search("py")
        self.assertEqual(3, len(res))

    def test_integration(self):
        s = services.CartService()
        res = s.search("py")
        book = s.detail(res[0].id)
        cart = media.Cart()
        s.add_to_cart(book, cart)
        ok = s.validate(cart)
        self.assertTrue(ok)




