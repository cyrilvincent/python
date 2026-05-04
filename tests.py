import unittest
import tp_function

class MyTests(unittest.TestCase):

    def test_my_first_test(self):
        self.assertEqual(2, 1+1)

    def test_factorielle(self):
        result = tp_function.factorielle(5)
        self.assertEqual(121, result)
