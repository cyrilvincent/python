import unittest
import tp_function
import math

class MyTests(unittest.TestCase):

    def test_my_first_test(self):
        self.assertEqual(2, 1+1)

    def test_factorielle(self):
        result = tp_function.factorielle(5)
        self.assertEqual(120, result)
        print(result)

    def test_prime(self):
        result = tp_function.is_prime(7)
        self.assertTrue(result)

    def test_float(self):
        result = math.cos(math.pi)
        self.assertAlmostEqual(result, -1, delta=1e-3)

    def test_factorielle_negative(self):
        with self.assertRaises(ValueError):
            tp_function.factorielle(-1)

