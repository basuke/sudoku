import unittest

from sudoku.model.constraint import Constraint
from sudoku.model.board import Board
from sudoku.model.list import Cells


class TestConstraint(unittest.TestCase):
    def test_constraint_work_on_cell_available(self):
        board = Board("""
        123|...|...
        """)

        constraint = Constraint(
            Cells(board.cells((4, 1), (5, 1))),
            [4, 5]
        )
        board.add_constraint(constraint)

        # row is affected by the constraint.
        self.assertEqual(
            {6, 7, 8, 9},
            board.cell(7, 1).available_numbers
        )

        # box is affected by the constraint.
        self.assertEqual(
            {1, 2, 3, 6, 7, 8, 9},
            board.cell(5, 2).available_numbers
        )

        # column isn't affected by it.
        self.assertEqual(
            {1, 2, 3, 4, 5, 6, 7, 8, 9},
            board.cell(4, 4).available_numbers
        )
