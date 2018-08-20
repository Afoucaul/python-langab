import unittest
from langab.lisp import let


class TestLisp(unittest.TestCase):
    def test_let(self):
        self.assertEqual((let (a = 1, b = 2) (a + b)), 3)

    def test_let_2(self):
        self.assertEqual((let (c = 12) (2 * c)), 24)
