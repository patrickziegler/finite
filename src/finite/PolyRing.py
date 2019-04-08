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
from .Poly import Poly


_known_generators = {
    (2, 2): (1, 1, 1),
    (2, 3): (1, 0, 1, 1),
    (2, 4): (1, 0, 0, 1, 1),
    (2, 5): (1, 0, 0, 1, 0, 1),
    (2, 6): (1, 0, 0, 0, 0, 1, 1),
    (2, 7): (1, 0, 0, 0, 1, 0, 0, 1),
    (2, 8): (1, 0, 0, 0, 1, 1, 1, 0, 1)
}


def dec2repr(value, modulo):
    """
    Yields a decomposition of 'value' in the finite field with
    the given modulo beginning with its least significant coefficient

    :param value: value to decompose
    :param modulo: modulo of field to decompose to
    :return: yield coefficients beginning with least significant
    """
    q = int(value)

    while q > 0:
        q, r = divmod(q, modulo)
        yield r


def auto_cast_poly_ring(fn):

    def wrapper(self, other):
        if hasattr(other, "poly"):
            return fn(self, other)
        else:
            return fn(self, self.__class__(other))

    return wrapper


class PolyRing:

    poly_factory = Poly.factory(modulo=2)
    generator = poly_factory(1, 0, 1, 1)
    power = 3

    @staticmethod
    def factory(modulo=2, power=3):
        class cls(PolyRing):
            pass

        cls.poly_factory = Poly.factory(modulo=modulo)

        key = (modulo, power)
        if key in _known_generators.keys():
            cls.generator = cls.poly_factory(*_known_generators[key])
        else:
            raise NotImplementedError("Search for generator polynomials currently not implemented!")

        cls.power = power
        cls.__name__ = "GF" + str(cls.poly_factory.field.modulo) + "^" + str(power)

        return cls

    @classmethod
    def __len__(cls):
        return cls.poly_factory.field.modulo ** cls.power

    @classmethod
    def elements(cls):
        """
        :return: yields all *non-zero* elements of this polynomial ring
        """
        for value in range(1, cls.poly_factory.field.modulo ** cls.power):
            yield cls(value)

    def __init__(self, value):
        if hasattr(value, "poly") or hasattr(value, "coeff"):
            _, self.poly = divmod(
                value,
                self.generator
            )
        else:
            _, self.poly = divmod(
                self.poly_factory(
                    np.flip(
                        np.asarray(
                            [c for c in dec2repr(value, self.poly_factory.field.modulo)]
                        )
                    )
                ),
                self.generator
            )

    def __repr__(self):
        return self.poly.__repr__()

    def __abs__(self):
        return abs(self.poly)

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

    @auto_cast_poly_ring
    def __divmod__(self, other):
        q, r = divmod(self.poly, other.poly)
        return self.__class__(q), self.__class__(r)

    def as_decimal(self):
        degree = len(self.poly.coeff) - 1
        return np.sum(
            [c.value * self.poly.field.modulo ** (degree - i) for i, c in enumerate(self.poly.coeff)]
        )

    def as_monic(self):
        return self.poly.as_monic()

    def trim(self):
        return self.poly.trim()

    def lc(self):
        return self.poly.lc()

    def at(self, x):
        return self.poly.at(x)
