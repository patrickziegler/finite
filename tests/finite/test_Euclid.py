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


class EuclidTest(unittest.TestCase):

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
