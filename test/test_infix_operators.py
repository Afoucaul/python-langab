import unittest
from langab.infix_operators import Infix


class TestInfixOperators(unittest.TestCase):
    def test_with_or(self):
        T = Infix(lambda x, y: x + y)

        self.assertEqual(1 |T| 2, 3)

    def test_with_comparators(self):
        M = Infix(lambda x, y: x * y)

        self.assertEqual(2 <<M>> 3, 6)
