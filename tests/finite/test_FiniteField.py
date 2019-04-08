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


class FiniteFieldTest(unittest.TestCase):

    def test_finite_field_1(self):
        z2 = FiniteField.factory(modulo=2)
        a, b = z2(0), z2(0)
        self.assertEqual(a + b, 0)
        self.assertEqual(a - b, 0)
        self.assertEqual(a * b, 0)
        self.assertEqual(a / b, 0)

    def test_finite_field_2(self):
        z2 = FiniteField.factory(modulo=2)
        a, b = z2(0), z2(1)
        self.assertEqual(a + b, 1)
        self.assertEqual(a - b, 1)
        self.assertEqual(a * b, 0)
        self.assertEqual(a / b, 0)

    def test_finite_field_3(self):
        z2 = FiniteField.factory(modulo=2)
        a, b = z2(1), z2(0)
        self.assertEqual(a + b, 1)
        self.assertEqual(a - b, 1)
        self.assertEqual(a * b, 0)
        self.assertEqual(a / b, 0)

    def test_finite_field_4(self):
        z2 = FiniteField.factory(modulo=2)
        a, b = z2(1), z2(1)
        self.assertEqual(a + b, 0)
        self.assertEqual(a - b, 0)
        self.assertEqual(a * b, 1)
        self.assertEqual(a / b, 1)

    def test_finite_field_5(self):
        z23 = FiniteField.factory(modulo=23)
        a, b = z23(7), z23(7)
        self.assertEqual(b.inverse(), z23(10))
        self.assertEqual(a / b, 1)
