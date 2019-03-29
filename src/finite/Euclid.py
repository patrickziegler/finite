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


def extended_euclidean(a, b):
    """
    Computes x and y as defined in a*x + b*y = gcd(a, b), see [1] for details

    [1] https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

    :param a: first operand
    :param b: second operand
    :return: x, y
    """
    if abs(b) > abs(a):
        x, y, gcd = extended_euclidean(b, a)
        return y, x, gcd

    if abs(b) == 0:
        return 1, 0, a

    gcd, gcd_buf = a, b

    x, x_buf = 1, 0
    y, y_buf = 0, 1

    while abs(gcd_buf) > 0:

        q, r = divmod(gcd, gcd_buf)

        gcd, gcd_buf = gcd_buf, r

        x = x - q * x_buf
        y = y - q * y_buf

        x, x_buf = x_buf, x
        y, y_buf = y_buf, y

    return x, y, gcd


def gcd(a, b):
    """
    Computes the greatest common divisor of a and b

    :param a: first operand
    :param b: second operand
    :return: gcd
    """
    if abs(b) > abs(a):
        return gcd(b, a)

    if abs(b) == 0:
        return a

    gcd_val, gcd_buf = a, b

    while abs(gcd_buf) > 0:

        _, r = divmod(gcd_val, gcd_buf)

        gcd_val, gcd_buf = gcd_buf, r

    return gcd_val


def lcm(a, b):
    """
    Computes the least common multiple of a and b

    :param a: first operand
    :param b: second operand
    :return: lcm
    """
    if abs(b) > abs(a):
        return lcm(b, a)

    if abs(b) == 0:
        return a

    gcd_val, gcd_buf = a, b
    lcm_val, lcm_buf = 1, 0

    while abs(gcd_buf) > 0:

        q, r = divmod(gcd_val, gcd_buf)

        gcd_val, gcd_buf = gcd_buf, r
        lcm_val, lcm_buf = q * lcm_val + lcm_buf, lcm_val

    return lcm_val
