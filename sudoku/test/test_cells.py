from unittest import TestCase
from sudoku.model.list import Cells
from sudoku.model.cell import Cell


cells = Cells.make((1, 1, 9), (2, 1), (3, 1))
cell1, cell2, cell3 = cells


class TestCells(TestCase):
    def test_cells(self):
        self.assertIs(cells, cells.cells)

    def test_cells_creation(self):
        l = Cells.make([Cell(2, 1)])
        self.assertEqual(1, len(l))
        self.assertEqual(2, l[0].x)

        l = Cells.make((1 , 2, 3))
        self.assertEqual(1, len(l))
        self.assertEqual(3, l[0].number)

        l = Cells.make((1, 2), (2, 3), (3, 4))
        self.assertEqual(3, len(l))
        self.assertEqual(3, l[1].y)

    def test_empty_cells(self):
        l = cells.empty_cells

        self.assertEqual([cell2, cell3], l)
        self.assertIsInstance(l, Cells)

    def test_which_is(self):
        self.assertEqual(cells.which_has(9), [cell1])
        self.assertEqual(cells.which_has(7), [])

    def test_is_aligned(self):
        a = Cells.make((1, 1), (3, 1))
        self.assertTrue(a.is_aligned_x)
        self.assertFalse(a.is_aligned_y)

        b = Cells.make((1, 1), (4, 1), (9, 1))
        self.assertTrue(b.is_aligned_x)
        self.assertFalse(b.is_aligned_y)

        c = Cells.make((2, 1), (2, 3))
        self.assertFalse(c.is_aligned_x)
        self.assertTrue(c.is_aligned_y)

        d = Cells.make((2, 1), (2, 3), (2, 7))
        self.assertFalse(d.is_aligned_x)
        self.assertTrue(d.is_aligned_y)

        # empty cells is not aligned
        e = Cells()
        self.assertFalse(e.is_aligned_x)
        self.assertFalse(e.is_aligned_y)

        # one cell is not aligned
        f = Cells.make((5, 4))
        self.assertFalse(f.is_aligned_x)
        self.assertFalse(f.is_aligned_y)

