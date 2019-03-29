import unittest

from src.finite.FiniteField import FiniteField


class FiniteFieldTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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


if __name__ == '__main__':
    unittest.main()
