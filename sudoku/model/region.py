from .list import List, Cells


class Region(Cells):
    """
    Base class for Row, Column and Area. Implements common features.
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
        return sorted(numbers)

class Row(Region):
    @property
    def y(self):
        return self.identifier

    @property
    def is_row(self):
        return True


class Column(Region):
    @property
    def x(self):
        return self.identifier

    @property
    def is_column(self):
        return True


class Area(Region):
    @property
    def x(self):
        return self.identifier[0]

    @property
    def y(self):
        return self.identifier[1]

    pass