from unittest import TestCase
from sudoku.model.cell import Cell


class TestCell(TestCase):
    def test_instantiation(self):
        cell = Cell(1, 2)
        self.assertIsInstance(cell, Cell)
        self.assertIsNone(cell.board)
        self.assertFalse(cell)

        cell = Cell(4, 9, 8)
        self.assertTrue(cell)
        self.assertEqual(cell.number, 8)

        # It's okay to create cell with strange position
        # if it's not bound to the board
        cell = Cell(-100, 1234, 33)
        self.assertEqual(cell.number, 33)

    def test_properties(self):
        cell = Cell(3, 4)

        self.assertEqual(cell.x, 3)
        self.assertEqual(cell.y, 4)
        self.assertEqual(cell.position, (3, 4))
        self.assertIsNone(cell.number)

        cell = Cell(2, 9, number=7)
        self.assertEqual(cell.number, 7)

    def test_equality(self):
        cell = Cell(3, 6)

        self.assertEqual(cell, Cell(3, 6))
        self.assertNotEqual(cell, Cell(3, 6, number=2))
        self.assertNotEqual(cell, Cell(6, 6))
        self.assertNotEqual(cell, Cell(3, 1))

    def test_comparison(self):
        cell = Cell(4, 5)

        self.assertGreater(cell, Cell(4, 4))
        self.assertGreater(cell, Cell(3, 5))

        self.assertGreaterEqual(cell, Cell(4, 4))
        self.assertGreaterEqual(cell, Cell(3, 5))

        self.assertLess(cell, Cell(4, 6))
        self.assertLess(cell, Cell(6, 5))

        self.assertLessEqual(cell, Cell(4, 6))
        self.assertLessEqual(cell, Cell(6, 5))

        cells = sorted([
            Cell(4, 7), Cell(3,9), Cell(2, 7),
            Cell(3, 7), Cell(5, 1), Cell(5, 4),
            Cell(5, 2),
        ])
        self.assertEqual([
            Cell(5, 1),
            Cell(5, 2),
            Cell(5, 4),
            Cell(2, 7), Cell(3, 7), Cell(4, 7),
            Cell(3, 9)
        ], cells)

    def test_board_regions(self):
        board = MockBoard()

        cell = Cell(5, 4, board=board)
        self.assertEqual("row 4", cell.row)
        self.assertEqual("column 5", cell.column)
        self.assertEqual("box 2, 2", cell.box)

        cell = Cell(1, 1, board=board)
        self.assertEqual("row 1", cell.row)
        self.assertEqual("column 1", cell.column)
        self.assertEqual("box 1, 1", cell.box)

        cell = Cell(9, 9, board=board)
        self.assertEqual("row 9", cell.row)
        self.assertEqual("column 9", cell.column)
        self.assertEqual("box 3, 3", cell.box)

    def test_board_related_exceptions(self):
        cell = Cell(1, 1)

        self.assertRaises(ReferenceError, lambda: cell.row)
        self.assertRaises(ReferenceError, lambda: cell.column)
        self.assertRaises(ReferenceError, lambda: cell.box)


class MockBoard(object):
    def row(self, y):
        return "row %d" % y

    def column(self, y):
        return "column %d" % y

    def box(self, x, y):
        return "box %d, %d" % (x, y)
