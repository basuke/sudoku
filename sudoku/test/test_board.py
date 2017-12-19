import unittest

from sudoku.model.board import Board
from sudoku.model import Cell
from sudoku.test import sample


class TestBoard(unittest.TestCase):
    def test_cell_access(self):
        board = Board(sample.EASY1)

        self.assertEqual(6, board.cell(2, 1).number)
        self.assertFalse(board.cell(5, 5))

    def test_region_access(self):
        board = Board(sample.EASY1)

        self.assertEqual(5, board.row(5).y)
        self.assertEqual((2, 3), board.area(2, 3).identifier)
        self.assertEqual(3, board.column(3).x)

    def test_finished(self):
        self.assertTrue(Board(sample.FINISHED1).is_finished)
        self.assertFalse(Board(sample.LAST_CELL1).is_finished)

    def test_validity(self):
        self.assertTrue(Board(sample.FINISHED1).is_valid)
        self.assertTrue(Board(sample.LAST_CELL1).is_valid)
        self.assertFalse(Board(sample.INVALID1).is_valid)

        board = Board(sample.INVALID1)
        invalids = board.all_invalid_regions_and_cells

        self.assertEqual(2, len(invalids))

        region, cells = invalids.pop(0)
        self.assertTrue(region.is_row)
        self.assertEqual(3, region.y)
        self.assertEqual([Cell(6,3,8), Cell(8,3,8)], cells)

        region, cells = invalids.pop(0)
        self.assertTrue(region.is_column)
        self.assertEqual(8, region.x)
        self.assertEqual([Cell(8,3,8), Cell(8,5,8)], cells)
