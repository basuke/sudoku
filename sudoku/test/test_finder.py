import unittest

from sudoku.finder.last_one import LastOneFinder
from sudoku.model.board import Board
from sudoku.solver import Solver


class TestFinder(unittest.TestCase):
    def setUp(self):
        pass

    def test_last_one(self):
        finder = LastOneFinder()
        board = Board("""
            2 1 4 | 6 9 3 | 7 5 8
            9 5 7 | 2 1 8 | 3 6 4
            6 3 8 | 5 7 4 | 2 9 1
            ------+-------+------
            4 6 3 | . 8 5 | 1 2 7
            1 7 9 | 4 6 2 | 8 3 5
            8 2 5 | 7 3 1 | 6 4 9
            ------+-------+------
            5 8 6 | 1 2 9 | 4 7 3
            7 4 1 | 3 5 6 | 9 8 2
            3 9 2 | 8 4 7 | 5 1 6
        """)

        self.assertFalse(board.is_complete)
        result = finder.find(board)
        self.assertTrue(result)
        self.assertEqual((4, 4), result.cell.position)
        self.assertFalse(result.cell)
        self.assertEqual(9, result.number)

        result.cell.set(9)

        self.assertTrue(board.is_complete)

    def test_solve_by_last_one(self):
        finder = LastOneFinder()
        board = Board("""
            2 1 4 | 6 9 3 | 7 5 8
            9 5 7 | 2 1 . | . . 4
            6 3 8 | 5 7 4 | 2 9 .
            ------+-------+------
            4 6 3 | . 8 . | 1 2 7
            1 7 9 | 4 6 2 | 8 3 5
            8 2 5 | 7 3 1 | 6 4 .
            ------+-------+------
            5 8 6 | 1 2 9 | 4 7 3
            7 4 1 | 3 . . | 9 8 2
            3 9 2 | 8 4 7 | 5 1 6
        """)

        solver = Solver(board, [finder])
        solver.solve()
        print [result.cell for result in solver.steps]
        self.assertTrue(solver.solve())
        self.assertTrue(board.is_complete)
