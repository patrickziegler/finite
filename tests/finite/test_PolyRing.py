# Copyright (C) 2019 Patrick Ziegler
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from finite import *
import unittest


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
