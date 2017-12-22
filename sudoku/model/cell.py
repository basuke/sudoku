from sudoku.stringify import stringify_board, stringify_cell

injected = []


class Injectable(object):
    @classmethod
    def inject(cls, name, method):
        setattr(cls, name, method)
        injected.append((cls, name))

    @staticmethod
    def reset():
        for cls, name in injected:
            if hasattr(cls, name):
                delattr(cls, name)


class Cell(Injectable):
    def __init__(self, x, y, number=None, board=None):
        self.position = (x, y)
        self.number = number
        self.board = board

    def __eq__(self, other):
        if type(other) == int:
            return self.number == other

        if self.__class__ != other.__class__:
            return False

        return self._sort_key == other._sort_key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self._sort_key > other._sort_key

    def __ge__(self, other):
        return self._sort_key >= other._sort_key

    def __le(self, other):
        return self._sort_key <= other._sort_key

    def __lt__(self, other):
        return self._sort_key < other._sort_key

    def __nonzero__(self):
        return self.number is not None

    def __str__(self):
        return stringify_cell(self)

    def __repr__(self):
        return stringify_cell(self, detail=True)

    @property
    def cells(self):
        from .list import Cells
        return Cells([self])

    @property
    def row(self):
        if not self.board:
            raise ReferenceError("this cell is not bound to any board")

        return self.board.row(self.y)

    @property
    def column(self):
        if not self.board:
            raise ReferenceError("this cell is not bound to any board")

        return self.board.column(self.x)

    @property
    def area(self):
        """area that the cell belongs to"""
        if not self.board:
            raise ReferenceError("this cell is not bound to any board")

        return self.board.area(
            int((self.x - 1) / 3) + 1,
            int((self.y - 1) / 3) + 1)

    @property
    def effective_cells(self):
        from .list import Cells
        return Cells(self.row + self.column + self.area)

    def set(self, number):
        assert self.number is None
        self.number = number
        return self

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def _sort_key(self):
        return (self.y, self.x, self.number)


