import unittest

from sudoku.model.constraint import Constraint
from sudoku.model.board import Board
from sudoku.model.list import Cells


class TestConstraint(unittest.TestCase):
    def test_constraint_work_on_cell_available(self):
        board = Board("""
        123|...|...
        """)

        # cells are in same box
        board.add_constraint(
            board.cells((4, 1), (5, 1)),
            4
        )

        # row is affected by the constraint.
        self.assertEqual(
            {5, 6, 7, 8, 9},
            board.cell(7, 1).available_numbers
        )

        # box is affected by the constraint.
        self.assertEqual(
            {1, 2, 3, 5, 6, 7, 8, 9},
            board.cell(5, 2).available_numbers
        )

        # column isn't affected by it.
        self.assertEqual(
            {1, 2, 3, 4, 5, 6, 7, 8, 9},
            board.cell(4, 4).available_numbers
        )

    def test_constraint_work_on_cell_available2(self):
        board = Board("""
        123|...|...
        """)

        # cells aren't in same box
        board.add_constraint(
            board.cells((4, 1), (7, 1)),
            4
        )

        # row is affected by the constraint.
        self.assertEqual(
            {5, 6, 7, 8, 9},
            board.cell(9, 1).available_numbers
        )

        # box isn't affected by the constraint.
        self.assertEqual(
            {1, 2, 3, 4, 5, 6, 7, 8, 9},
            board.cell(5, 2).available_numbers
        )

        # column isn't affected by it.
        self.assertEqual(
            {1, 2, 3, 4, 5, 6, 7, 8, 9},
            board.cell(4, 4).available_numbers
        )
