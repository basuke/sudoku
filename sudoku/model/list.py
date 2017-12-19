from sudoku.stringify import stringify_list
from .cell import Cell


def N(x):
    return x


class List(list):
    @property
    def is_row(self):
        return False

    @property
    def is_column(self):
        return False

    def contains(self, item):
        return item in self

    @property
    def class_for_copy(self):
        return List

    def copy(self, iterable=None):
        return self.class_for_copy(iterable if iterable is not None else self)

    def filter(self, fn=N):
        return self.copy(item for item in self if fn(item))

    def map(self, fn=N):
        return self.copy(fn(item) for item in self)

    def __and__(self, other):
        return self.copy(sorted(set(self) & set(other)))

    def __or__(self, other):
        return self.copy(sorted(set(self) | set(other)))

    def __sub__(self, other):
        return self.copy(sorted(set(self) - set(other)))

    @property
    def cells(self):
        """all cells recursively"""
        result = []
        for item in self:
            if type(item) == Cell:
                result.append(item)
            elif hasattr(item, 'cells'):
                result += item.cells

        return Cells(result)

    def some(self, fn):
        for cell in self:
            if fn(cell):
                return True
        return False

    def all(self, fn):
        for cell in self:
            if not fn(cell):
                return False
        return True

    def __repr__(self):
        return stringify_list(self, True)

    def __str__(self):
        return stringify_list(self, False)


class Cells(List):
    def __init__(self, *cells):
        if len(cells) == 1 and type(cells[0]) == tuple:
            cells = [[Cell(*cells[0])]]
        elif len(cells) > 1:
            cells = [(Cell(*cell) if type(cell) == tuple else cell for cell in cells)]

        super(Cells, self).__init__(*cells)
        assert self.all(lambda cell: type(cell) == Cell)

    @property
    def class_for_copy(self):
        return Cells

    @property
    def cells(self):
        return self

    @property
    def empty_cells(self):
        return self.filter(lambda c: not c)

    def which_has(self, number):
        return self.filter(lambda c: c.number == number)

    @property
    def filled_cells(self):
        return self.filter(lambda c: c)

    def other_cells(self, cell):
        return self.filter(lambda c: c != cell)

    @property
    def is_aligned_x(self):
        if len(self) < 2:
            return False
        return self.all(lambda c: c.y == self[0].y)

    @property
    def is_aligned_y(self):
        if len(self) < 2:
            return False
        return self.all(lambda c: c.x == self[0].x)

