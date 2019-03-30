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


import numpy as np
from finite.FiniteField import FiniteField


def auto_cast_poly(fn):

    def wrapper(self, other):
        if hasattr(other, "coeff"):
            try:
                if (self.field is None and other.field is None) or \
                        (self.field.modulo == other.field.modulo):

                    return fn(self, other)

            except AttributeError:
                pass

            raise ValueError("Operands must be defined over the same finite domain!")

        else:
            return fn(self, self.__class__(other))

    return wrapper


class Poly:

    field = None

    @staticmethod
    def factory(modulo):
        class cls(Poly):
            pass

        cls.field = FiniteField.factory(modulo=modulo)
        cls.__name__ = "Poly over Z/%d" % cls.field.modulo

        return cls

    def __init__(self, *args):
        if self.field is None:
            self.coeff = np.asarray(args)
        else:
            self.coeff = np.asarray([self.field(arg) for arg in args])

        self.trim()

    @classmethod
    def from_array(cls, coeff):
        return cls(*coeff).trim()

    def __repr__(self):
        return " + ".join([str(c) + "*X^" + str(len(self.coeff) - i - 1) for i, c in enumerate(self.coeff)])

    def __abs__(self):
        """
        :return: the polynomials degree
        """
        return len(self.coeff) - 1

    @auto_cast_poly
    def __eq__(self, other):
        return np.all(self.coeff == other.coeff)

    @auto_cast_poly
    def __ne__(self, other):
        return not self == other

    @auto_cast_poly
    def __add__(self, other):
        return self.from_array(np.polyadd(self.coeff, other.coeff))

    @auto_cast_poly
    def __radd__(self, other):
        return self.from_array(np.polyadd(other.coeff, self.coeff))

    @auto_cast_poly
    def __sub__(self, other):
        return self.from_array(np.polysub(self.coeff, other.coeff))

    @auto_cast_poly
    def __rsub__(self, other):
        return self.from_array(np.polysub(other.coeff, self.coeff))

    @auto_cast_poly
    def __mul__(self, other):
        return self.from_array(np.polymul(self.coeff, other.coeff))

    @auto_cast_poly
    def __rmul__(self, other):
        return self.from_array(np.polymul(other.coeff, self.coeff))

    @auto_cast_poly
    def __truediv__(self, other):
        q, _ = self.__divmod__(other)
        return q

    @auto_cast_poly
    def __rtruediv__(self, other):
        q, _ = other.__divmod__(self)
        return q

    @auto_cast_poly
    def __divmod__(self, other):
        """
        This is an implementation of the Polynomial Long Division

        :param other: other polynomial as divisor
        :return: tuple containing quotient and remainder
        """
        diff = abs(self) - abs(other)

        if diff < 0:
            return 0, self.from_array(self.coeff)

        q = [0] * (diff + 1)
        r = self.from_array(self.coeff)

        zero = self.__class__(0)

        for i in range(len(q)):

            q[i] = r.lc() / other.lc()
            r = r - other * self.from_array([q[i]] + [0] * (abs(r) - abs(other)))

            if r.trim() == zero:
                break

        return self.from_array(q), r

    def as_monic(self):
        """
        :return: copy of this polynomial with all coefficients
        divided by the most significant one
        """
        p = self.from_array(self.coeff)
        p.coeff /= self.coeff[0]
        return p

    def trim(self):
        try:
            if self.coeff[0] == 0:
                i = np.where(self.coeff != 0)[0][0]
                self.coeff = self.coeff[i::]

        except IndexError:
            self.coeff = [0]

        return self

    def lc(self):
        try:
            return self.coeff[0]

        except IndexError:
            return 0

    def at(self, x):
        """
        Evaluates the polynomial at 'x' using Horner's Method

        :param x: any number or object of type 'Domain'
        :return: the same
        """
        value = 0

        for c in self.coeff:
            value = c + x * value

        return value
