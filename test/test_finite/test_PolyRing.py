import unittest

from finite import *


class PolyRingTest(unittest.TestCase):

    def test_poly_ring_1(self):
        PolyMod2 = Poly.factory(modulo=2)
        self.assertEqual(PolyRing(13), PolyMod2(1, 1, 0))

    def test_poly_ring_2(self):
        GF8 = PolyRing.factory(modulo=2, power=3)
        PolyMod2 = Poly.factory(modulo=2)

        p1 = PolyMod2(1, 0, 0, 1, 1)
        p2 = PolyMod2(1, 1, 0, 1, 0)

        p1gf2 = GF8(p1)
        p2gf2 = GF8(p2)

        s = p1 + p2
        sgf2 = p1gf2 + p2gf2

        self.assertEqual(s, PolyMod2(1, 0, 0, 1))
        self.assertEqual(sgf2, PolyMod2(1, 0))

    def test_poly_ring_3(self):
        GF8 = PolyRing.factory(modulo=2, power=3)
        PolyMod2 = Poly.factory(modulo=2)

        p1 = PolyMod2(1, 0, 1)
        p2 = PolyMod2(1, 1, 1)

        p1gf2 = GF8(p1)
        p2gf2 = GF8(p2)

        s = p1 * p2
        sgf2 = p1gf2 * p2gf2

        self.assertEqual(s, PolyMod2(1, 1, 0, 1, 1))
        self.assertEqual(sgf2, PolyMod2(1, 1, 0))


if __name__ == '__main__':
    unittest.main()