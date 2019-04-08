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


class PolyTest(unittest.TestCase):

    def test_poly_1(self):
        PolyMod2 = Poly.factory(modulo=2)
        p1 = PolyMod2(1, 2, 3, 4)
        p2 = PolyMod2(2, 3, 4, 5)
        self.assertEqual(p1 + p2, PolyMod2(1, 1, 1, 1))
        self.assertEqual(p1 * p2, PolyMod2(1, 0, 0, 0, 1, 0))

    def test_poly_2(self):
        p1 = Poly(3, 9, 7)
        p2 = Poly(1, 5)
        q, r = divmod(p1, p2)
        self.assertEqual(q, Poly(3, -6))
        self.assertEqual(r, Poly(37))

    def test_poly_3(self):
        PolyMod2 = Poly.factory(modulo=2)
        p1 = PolyMod2(1, 1, 0, 0)
        p2 = PolyMod2(1, 0, 1, 1)
        q, r = divmod(p1, p2)
        self.assertEqual(q, PolyMod2(1))
        self.assertEqual(r, PolyMod2(1, -1, -1))

    def test_poly_4(self):
        PolyMod13 = Poly.factory(modulo=13)
        z13 = PolyMod13.field
        p = PolyMod13(6, 9, 12, 11, 2, 2)
        a = 6
        v = [p.at(z13(a ** k)) for k in range(12)]
        ref = [z13(x) for x in [3, 1, 4, 7, 8, 1, 2, 8, 5, 6, 3, 2]]
        self.assertEqual(v, ref)
