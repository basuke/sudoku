from .list import Cells


class Constraint(Cells):
    def __init__(self, cells, numbers):
        super(Constraint, self).__init__(cells)
        self.numbers = set(numbers)

        assert len(self) == len(self.numbers)

    def __contains__(self, item):
        if item in self.numbers:
            return True

        return super(Constraint, self).__contains__(item)
