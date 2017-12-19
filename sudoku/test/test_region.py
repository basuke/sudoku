import unittest

from sudoku.model import Cell
from sudoku.model.region import Region


class TestRegion(unittest.TestCase):
    def test_equality(self):
        a = Region('hello', [])

        self.assertEqual(Region('hello', []), a)
        self.assertNotEqual(Region('hello', [Cell(1, 2)]), a)
        self.assertNotEqual(Region(1234, []), a)

        

