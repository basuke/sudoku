from .list import Cells
from sudoku.stringify import stringify_list


class Constraint(Cells):
    def __init__(self, cells):
        super(Constraint, self).__init__(cells)
        self.numbers = set()

    def add_number(self, number):
        self.numbers.add(number)

    @property
    def is_complete(self):
        return len(self) == len(self.numbers)

    def __contains__(self, item):
        if item in self.numbers:
            return True

        return super(Constraint, self).__contains__(item)

    def __repr__(self):
        return stringify_list(self, detail=True) + " = " + repr(sorted(self.numbers))

    def __str__(self):
        return self.__repr__()