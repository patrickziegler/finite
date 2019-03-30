import unittest

from src.finite.Euclid import extended_euclidean, gcd, lcm
from src.finite.FiniteField import FiniteField
from src.finite.Poly import Poly


class EuclidTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_euclid_1(self):
        a = 4864
        b = 3458
        self.assertEqual(extended_euclidean(a, b), (32, -45, 38))
        self.assertEqual(gcd(a, b), 38)
        self.assertEqual(lcm(a, b), 128)

    def test_euclid_2(self):
        a = Poly(1, 7, 6)
        b = Poly(1, -5, -6)
        d = gcd(a, b).as_monic()
        self.assertEqual(d, Poly(1, 1))

    def test_euclid_3(self):
        PolyMod13 = Poly.factory(modulo=13)
        a = PolyMod13(1, 6, 11, 6)
        b = PolyMod13(2, 7, 7, 12)
        d = gcd(a, b).as_monic()
        self.assertEqual(d, PolyMod13(1, 3))


if __name__ == '__main__':
    unittest.main()
