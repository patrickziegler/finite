import unittest

from src.finite.FiniteField import FiniteField
from src.finite.Poly import Poly
from src.finite.PolyRing import GaloisField


class PolyRingTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_poly_ring_1(self):
        poly = Poly.factory(field=FiniteField.factory(modulo=2))
        self.assertEqual(GaloisField(13), poly(1, 1, 0))

    def test_poly_ring_2(self):
        gf2 = GaloisField.factory(power=3)
        poly = Poly.factory(field=gf2.FIELD)

        p1 = poly(1, 0, 0, 1, 1)
        p2 = poly(1, 1, 0, 1, 0)

        p1gf2 = gf2(p1)
        p2gf2 = gf2(p2)

        s = p1 + p2
        sgf2 = p1gf2 + p2gf2

        self.assertEqual(s, poly(1, 0, 0, 1))
        self.assertEqual(sgf2, poly(1, 0))

    def test_poly_ring_3(self):
        gf2 = GaloisField.factory(power=3)
        poly = Poly.factory(field=gf2.FIELD)

        p1 = poly(1, 0, 1)
        p2 = poly(1, 1, 1)

        p1gf2 = gf2(p1)
        p2gf2 = gf2(p2)

        s = p1 * p2
        sgf2 = p1gf2 * p2gf2

        self.assertEqual(s, poly(1, 1, 0, 1, 1))
        self.assertEqual(sgf2, poly(1, 1, 0))


if __name__ == '__main__':
    unittest.main()
