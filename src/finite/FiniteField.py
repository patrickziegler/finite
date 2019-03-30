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


from .Euclid import extended_euclidean


def auto_cast_finite_field(fn):

    def wrapper(self, other):
        if hasattr(other, "value"):
            return fn(self, other)
        else:
            return fn(self, self.__class__(other))

    return wrapper


class FiniteField:

    modulo = 2

    @staticmethod
    def factory(modulo=2):
        class cls(FiniteField):
            pass

        cls.modulo = modulo
        cls.__name__ = "Z/%d" % modulo

        return cls

    @classmethod
    def __len__(cls):
        return cls.modulo

    @classmethod
    def elements(cls):
        """
        :return: yields all *non-zero* field elements
        """
        for element in range(1, cls.modulo):
            yield element

    def __init__(self, value):
        try:
            self.value = value % self.modulo
        except TypeError:
            self.value = value.value % self.modulo

    def __repr__(self):
        return "(" + str(self.value) + " mod " + str(self.modulo) + ")"

    def __abs__(self):
        return abs(self.value)

    def __float__(self):
        return float(self.value)

    @auto_cast_finite_field
    def __eq__(self, other):
        return self.value == other.value % self.modulo

    @auto_cast_finite_field
    def __ne__(self, other):
        return not self == other

    @auto_cast_finite_field
    def __add__(self, other):
        return self.__class__(self.value + other.value)

    @auto_cast_finite_field
    def __radd__(self, other):
        return self.__class__(other.value + self.value)

    @auto_cast_finite_field
    def __sub__(self, other):
        return self.__class__(self.value - other.value)

    @auto_cast_finite_field
    def __rsub__(self, other):
        return self.__class__(other.value - self.value)

    @auto_cast_finite_field
    def __mul__(self, other):
        return self.__class__(self.value * other.value)

    @auto_cast_finite_field
    def __rmul__(self, other):
        return self.__class__(other.value * self.value)

    @auto_cast_finite_field
    def __truediv__(self, other):
        return self * other.inverse()

    @auto_cast_finite_field
    def __rtruediv__(self, other):
        return other.inverse() * self

    @auto_cast_finite_field
    def __divmod__(self, other):
        q, r = divmod(self.value, other.value)
        return self.__class__(q), self.__class__(r)

    def inverse(self):
        x, _, _ = extended_euclidean(self.value, self.modulo)
        return self.__class__(x)
