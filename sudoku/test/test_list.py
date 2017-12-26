from unittest import TestCase
from sudoku.model.list import List
from sudoku.model.cell import Cell


def cell(x, y, number=None):
    return Cell(x, y, number)


cell1, cell2, cell3 = cell(1,1,9), cell(2,1), cell(3,1)


class TestList(TestCase):
    def test_equal(self):
        self.assertEqual(List([1, 2, 3]), List([1, 2, 3]))
        self.assertEqual(List(), List())

    def test_property(self):
        lst = List([1, 2, 3])

        self.assertTrue(hasattr(lst, 'is_row'))
        self.assertTrue(hasattr(lst, 'is_column'))
        self.assertFalse(lst.is_row)
        self.assertFalse(lst.is_column)

    def test_coy(self):
        lst = List(range(0, 10))

        self.assertEqual(lst, lst.copy())
        self.assertEqual([], lst.copy([]))
        self.assertIsInstance(lst, List)

        # copy is not the same object, but same value
        self.assertIsNot(lst, lst.copy())

    def test_filter(self):
        lst = List(range(0, 10))

        self.assertEqual([0, 3, 6, 9], lst.filter(lambda x: x % 3 == 0))

    def test_map(self):
        lst = List(range(0, 5))

        self.assertEqual([0, 2, 4, 6, 8], lst.map(lambda x: x * 2))

    def test_set_operations(self):
        l1 = List(range(0, 5))
        l2 = List(range(0, 10, 2))

        self.assertEqual([0, 2, 4], l1 & l2)
        self.assertEqual([0, 1, 2, 3, 4, 6, 8], l1 | l2)
        self.assertEqual([1, 3], l1 - l2)

        self.assertIsInstance(l1 & l2, List)
        self.assertIsInstance(l1 | l2, List)
        self.assertIsInstance(l1 - l2, List)

    def test_subset(self):
        l1 = List([1, 2, 3, 4, 5, 6])

        self.assertTrue(List([1, 2, 3]) in l1)
        self.assertTrue(List([]) in l1)
        self.assertTrue(l1 in l1)
        self.assertTrue(List([6]) in l1)

        self.assertFalse(List([8]) in l1)
        self.assertFalse(List([1, 2, 7]) in l1)

    def test_cells(self):
        self.assertEqual([], List([1, 2, 3]).cells)

        self.assertEqual([cell1, cell2], List([cell1, cell2]).cells)

        # self.assertEqual([cell1, cell2, cell3], List([
        #     cell1,
        #     List([1, 2, List([cell2])]),
        #     List([cell3])
        # ]).cells)

    def test_some(self):
        l = List([cell1, cell2, cell3])

        self.assertTrue(l.some(lambda cell: cell == 9))
        self.assertFalse(l.some(lambda cell: cell == 8))
        self.assertFalse(List([]).some(lambda cell: True))

    def test_all(self):
        l = List([cell1, cell2, cell3])

        self.assertTrue(l.all(lambda cell: cell.y == 1))
        self.assertFalse(l.all(lambda cell: cell.x == 2))
        self.assertFalse(l.all(lambda cell: cell))
        self.assertTrue(List([]).all(lambda cell: False))
