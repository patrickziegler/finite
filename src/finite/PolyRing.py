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
from .FiniteField import FiniteField
from .Poly import Poly


def dec2bin(value, width):
    """
    Returns a binary representation array of the given decimal input,
    negative values will be returned as two's complement

    :param value: decimal value
    :param width: bit-depth
    :return: binary representation array
    """
    if value < 0:
        mask = np.sum(np.power(2, range(0, width)))
        value = (value ^ mask) + 1

    digits = []
    q = abs(value)

    while q > 0:
        q, r = divmod(q, 2)
        digits.append(r)

    return np.flip(np.asarray(digits))


def auto_cast_poly_ring(fn):

    def wrapper(self, other):
        if hasattr(other, "poly"):
            return fn(self, other)
        else:
            return fn(self, self.__class__(other))

    return wrapper


class GaloisField:

    FIELD = FiniteField.factory(modulo=2)
    POLY_FACTORY = Poly.factory(field=FIELD)
    GENERATOR = POLY_FACTORY(1, 0, 1, 1)
    POWER = 3

    @staticmethod
    def factory(power=3):
        known_generators = {
            2: (1, 1, 1),
            3: (1, 0, 1, 1),
            4: (1, 0, 0, 1, 1),
            5: (1, 0, 0, 1, 0, 1),
            6: (1, 0, 0, 0, 0, 1, 1),
            7: (1, 0, 0, 0, 1, 0, 0, 1),
            8: (1, 0, 0, 0, 1, 1, 1, 0, 1)
        }

        class cls(GaloisField):
            pass

        if power in known_generators.keys():
            cls.GENERATOR = cls.POLY_FACTORY(*known_generators[power])
        else:
            raise NotImplementedError("Search for generator polynomials currently not implemented!")

        cls.POWER = power
        cls.__name__ = "GF2^" + str(power)

        return cls

    @classmethod
    def __len__(cls):
        return 2 ** cls.POWER

    @classmethod
    def elements(cls):
        """
        :return: yields all *nonzero* elements of this polynomial ring
        """
        for value in range(1, 2 ** cls.POWER):
            yield cls(value)

    def __init__(self, value):

        if hasattr(value, "coeff"):
            _, self.poly = divmod(
                value,
                self.GENERATOR
            )

        else:
            _, self.poly = divmod(
                self.POLY_FACTORY(*dec2bin(value, width=2**self.POWER)),
                self.GENERATOR
            )

    def __repr__(self):
        return self.poly.__repr__()

    @auto_cast_poly_ring
    def __eq__(self, other):
        return self.poly == other.poly

    @auto_cast_poly_ring
    def __ne__(self, other):
        return not self == other

    @auto_cast_poly_ring
    def __add__(self, other):
        return self.__class__(self.poly + other.poly)

    @auto_cast_poly_ring
    def __radd__(self, other):
        return self.__class__(other.poly + self.poly)

    @auto_cast_poly_ring
    def __sub__(self, other):
        return self.__class__(self.poly - other.poly)

    @auto_cast_poly_ring
    def __rsub__(self, other):
        return self.__class__(other.poly - self.poly)

    @auto_cast_poly_ring
    def __mul__(self, other):
        return self.__class__(self.poly * other.poly)

    @auto_cast_poly_ring
    def __rmul__(self, other):
        return self.__class__(other.poly * self.poly)

    @auto_cast_poly_ring
    def __truediv__(self, other):
        q, _ = self.__divmod__(other)
        return q

    @auto_cast_poly_ring
    def __rtruediv__(self, other):
        q, _ = other.__divmod__(self)
        return q

    def __pow__(self, power, modulo=None):
        return self.poly.__pow__(power, modulo)

    @auto_cast_poly_ring
    def __divmod__(self, other):
        q, r = divmod(self.poly, other.poly)
        return self.__class__(q), self.__class__(r)

    def trim(self):
        self.poly.trim()
        return self

    def lc(self):
        return self.poly.lc()

    def at(self, x):
        return self.poly.at(x)
