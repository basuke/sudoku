from .cell import Cell
from .list import Cells, List
from .region import Row, Column, Area
from ..parser import parse


class Board(Cells):
    def __init__(self, numbers_str=""):
        numbers = list(parse(numbers_str))

        def gen_cells():
            for y in range(1, 10):
                for x in range(1, 10):
                    number = numbers.pop(0) if numbers else None
                    yield Cell(x, y, number, board=self)

        super(Board, self).__init__(gen_cells())

        def gen_row(y):
            return Row(y, self.filter(lambda cell: cell.y == y), self)

        def gen_column(x):
            return Column(x, self.filter(lambda cell: cell.x == x), self)

        def gen_area(x, y):
            max_x = x * 3
            min_x = max_x - 3 + 1
            max_y = y * 3
            min_y = max_y - 3 + 1

            def in_area(cell):
                return min_x <= cell.x <= max_x and min_y <= cell.y <= max_y

            return Area(
                (x, y),
                self.filter(lambda cell: in_area(cell)),
                self
            )

        self.rows = List(gen_row(y) for y in range(1, 10))
        self.columns = List(gen_column(x) for x in range(1, 10))
        self.areas = List(gen_area(x, y) for y in range(1, 4) for x in range(1, 4))

        self.area_rows = List(List(area for area in self.areas if area.y == i) for i in range(1, 4))
        self.area_columns = List(List(area for area in self.areas if area.x == i) for i in range(1, 4))

        self.analyzers = []

    def cell(self, x, y):
        return self[(y - 1) * 9 + (x - 1)]

    def row(self, y):
        return self.rows[y - 1]

    def column(self, x):
        return self.columns[x - 1]

    def area(self, x, y):
        return self.areas[(y - 1) * 3 + (x - 1)]

    @property
    def is_finished(self):
        return len(self.empty_cells) == 0

    @property
    def is_valid(self):
        gen = self.find_invalid_regions_and_cells()

        try:
            if gen.next():
                return False
        except StopIteration:
            return True

    @property
    def is_complete(self):
        return self.is_finished and self.is_valid

    @property
    def all_invalid_regions_and_cells(self):
        return [(region, cells) for region, cells in self.find_invalid_regions_and_cells()]

    def find_invalid_regions_and_cells(self):
        for region in self.rows + self.columns + self.areas:
            cells = region.invalid_cells
            if cells:
                yield (region, cells)

    def analyze(self):
        for analyzer in self.analyzers:
            analyzer.analyze(self)

    def attach_analyzer(self, analyzer):
        try:
            pos = self.analyzers.index(analyzer)
            return self.analyzers[pos]
        except ValueError, e:
            analyzer.will_bind(self)
            self.analyzers.append(analyzer)
            return analyzer

