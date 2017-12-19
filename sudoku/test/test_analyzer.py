import unittest
from sudoku.model.board import Board
from sudoku.model.analyzer import Analyzer
from sudoku.model.cell import Cell, Injectable


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.board = Board("1.2.3.4.5.6.7.8.9")

    def tearDown(self):
        Injectable.reset()

    def test_add_analyzer(self):
        analyzer = MockAnalyzer()

        self.board.attach_analyzer(analyzer)
        self.assertEqual(1, analyzer.bound_count)

    def test_add_analyzer_twice(self):
        analyzer = MockAnalyzer()

        self.board.attach_analyzer(analyzer)

        # mark it
        self.assertIsNone(analyzer.name)
        analyzer.name = "Hello"

        another = MockAnalyzer()
        result = self.board.attach_analyzer(another)
        self.assertEqual("Hello", result.name)

    def test_equality(self):
        a = MockAnalyzer()
        b = MockAnalyzer()
        self.assertTrue(a == b)

    def test_analyze_is_called(self):
        a = MockAnalyzer()
        self.board.attach_analyzer(a)

        self.assertIsNone(a.passed_board)
        self.board.analyze()
        self.assertIsInstance(a.passed_board, Board)

    def test_property_extension(self):
        cell = self.board.cell(3, 1)

        self.assertRaises(
            AttributeError,
            lambda: cell.is_happy)
        self.assertRaises(
            AttributeError,
            lambda: cell.is_number(2))

        a = self.board.attach_analyzer(MockAnalyzer())

        self.assertEqual("Happy 3, 1", cell__is_happy.__get__(cell))
        self.assertEqual("Happy 3, 1", cell.is_happy)
        self.assertEqual(True, cell.is_number(2))


@property
def cell__is_happy(cell):
    return "Happy %s, %s" % cell.position


def cell__is_number(cell, number):
    return cell.number == number


class MockAnalyzer(Analyzer):
    def __init__(self):
        super(MockAnalyzer, self).__init__()
        self.bound_count = 0
        self.name = None
        self.passed_board = None

    def will_bind(self, board):
        self.bound_count += 1

        Cell.inject('is_happy', cell__is_happy)

        Cell.inject('is_number', cell__is_number)


    def analyze(self, board):
        self.passed_board = board
