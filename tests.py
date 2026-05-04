import unittest
import tp_function
import math
import tp_list


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


    def test_sum(self):
        result = tp_list.sum([1,2,3,4])
        self.assertEqual(10, result)

    def test_filter_even(self):
        result = tp_list.filter_even([1,2,3,4])
        self.assertEqual([2,4], result)

    def test_filter_prime(self):
        result = tp_list.filter_prime([1,2,3,4,5,6,7])
        self.assertEqual([2,3,5,7], result)

    def test_remove_all(self):
        result = tp_list.remove_all([1,333,2,333,3,333], 333)
        self.assertEqual([1,2,3], result)
