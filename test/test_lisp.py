import unittest
from langab.lisp import let


class TestLisp(unittest.TestCase):
    def test_let(self):
        self.assertEqual((let (a = 1, b = 2) (a + b)), 3)
