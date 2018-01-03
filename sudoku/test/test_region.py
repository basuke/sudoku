import unittest

from sudoku.model import Cell, Board
from sudoku.model.region import Region


class TestRegion(unittest.TestCase):
    def test_equality(self):
        a = Region('hello', [])

        self.assertEqual(Region('hello', []), a)
        self.assertNotEqual(Region('hello', [Cell(1, 2)]), a)
        self.assertNotEqual(Region(1234, []), a)

    def test_possible_cells(self):
        board = Board("""
        1.2|345|678
        ...|8..|...
        ...|127|..9
        """)

        self.assertEqual(
            [],
            board.box(1,1).possible_cells_with(1)
        )

        self.assertEqual(
            [],
            board.box(1, 1).possible_cells_with(2)
        )

        self.assertEqual(
            board.cells((1,2), (2,2), (3,2), (1,3), (2,3), (3,3)),
            board.box(1, 1).possible_cells_with(3)
        )

        self.assertEqual(
            board.cells((1,2), (2,2), (3,2), (1,3), (2,3), (3,3)),
            board.box(1, 1).possible_cells_with(4)
        )

        self.assertEqual(
            board.cells((1,2), (2,2), (3,2), (1,3), (2,3), (3,3)),
            board.box(1, 1).possible_cells_with(5)
        )

        self.assertEqual(
            board.cells((1,2), (2,2), (3,2), (1,3), (2,3), (3,3)),
            board.box(1, 1).possible_cells_with(6)
        )

        self.assertEqual(
            board.cells((1,2), (2,2), (3,2)),
            board.box(1, 1).possible_cells_with(7)
        )

        self.assertEqual(
            board.cells((1,3), (2,3), (3,3)),
            board.box(1, 1).possible_cells_with(8)
        )

        self.assertEqual(
            board.cells((2,1), (1,2), (2,2), (3,2)),
            board.box(1, 1).possible_cells_with(9)
        )

