from .list import List, Cells


class Region(Cells):
    """
    Base class for Row, Column and Box. Implements common features.
    """
    def __init__(self, identifier, cells, board=None):
        super(Region, self).__init__(cells)
        self.identifier = identifier
        self.board = board

    def __eq__(self, other):
        return super(Region, self).__eq__(other) and self.identifier == other.identifier

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def invalid_cells(self):
        def is_invalid_cell(cell):
            return self.other_cells(cell).contains(cell.number)

        return self.filled_cells.filter(is_invalid_cell)

    @property
    def available_numbers(self):
        numbers = set(range(1, 10))
        filled = set(cell.number for cell in self.filled_cells)
        numbers -= filled
        return numbers

    def possible_cells_with(self, number):
        if self.which_has(number):
            return Cells()

        return self.empty_cells.filter(lambda cell: number in cell.available_numbers)

    def crossing_cells(self, other):
        return other.filter(self.check_crossing)

    def crossing_cell(self, other):
        cells = self.crossing_cells(other)
        return cells[0] if cells else None

    def check_crossing(self, cell):
        return cell in self


class Row(Region):
    @property
    def y(self):
        return self.identifier

    @property
    def is_row(self):
        return True

    def check_crossing(self, cell):
        return cell.y == self.y


class Column(Region):
    @property
    def x(self):
        return self.identifier

    @property
    def is_column(self):
        return True

    def check_crossing(self, cell):
        return cell.x == self.x


class Box(Region):
    @property
    def x(self):
        return self.identifier[0]

    @property
    def y(self):
        return self.identifier[1]

    def cell(self, x, y):
        return self[(y - 1) * 3 + (x - 1)]

    @property
    def rows(self):
        return [self.cell(1, y).row for y in range(1, 4)]

    @property
    def columns(self):
        return [self.cell(x, 1).row for x in range(1, 4)]
