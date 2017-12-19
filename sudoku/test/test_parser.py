import unittest
from sudoku.parser import parse, parse2d


class TestParser(unittest.TestCase):
    def test_parse(self):
        result = parse("""
        123|456|789
        ...|...|...
        ...|...|...
        ---+---+---
        """)

        self.assertEqual([
            1,2,3,4,5,6,7,8,9,
            None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None,
        ], list(result))


    def test_parse2d(self):
        result = parse2d("""
        123|456|789
        ...|...|...
        ...|...|...
        ---+---+---
        """)

        self.assertEqual([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ], result)