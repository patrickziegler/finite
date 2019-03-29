import unittest

from src.finite.FiniteField import FiniteField
from src.finite.Poly import Poly


class PolyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_poly_1(self):
        poly = Poly.factory(field=FiniteField.factory(modulo=2))
        p1 = poly(1, 2, 3, 4)
        p2 = poly(2, 3, 4, 5)
        self.assertEqual(p1 + p2, poly(1, 1, 1, 1))
        self.assertEqual(p1 * p2, poly(1, 0, 0, 0, 1, 0))

    def test_poly_2(self):
        p1 = Poly(3, 9, 7)
        p2 = Poly(1, 5)
        q, r = divmod(p1, p2)
        self.assertEqual(q, Poly(3, -6))
        self.assertEqual(r, Poly(37))

    def test_poly_3(self):
        poly = Poly.factory(field=FiniteField.factory(modulo=2))
        p1 = poly(1, 1, 0, 0)
        p2 = poly(1, 0, 1, 1)
        q, r = divmod(p1, p2)
        self.assertEqual(q, poly(1))
        self.assertEqual(r, poly(1, -1, -1))

    def test_poly_4(self):
        z13 = FiniteField.factory(modulo=13)
        poly = Poly.factory(field=z13)
        p = poly(6, 9, 12, 11, 2, 2)
        a = 6
        v = [p.at(z13(a ** k)) for k in range(12)]
        ref = [z13(x) for x in [3, 1, 4, 7, 8, 1, 2, 8, 5, 6, 3, 2]]
        self.assertEqual(v, ref)


if __name__ == '__main__':
    unittest.main()
