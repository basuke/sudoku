from ..solver.finder import Finder
from ..model.constraint import Constraint


class ConstraintFinder(Finder):
    def find(self, board):
        for box in board.boxes:
            for constraint in self.find_constraint(box):
                board.add_constraint(constraint)

    def find_constraint(self, box):
        numbers = box.available_numbers
        cells = box.empty_cells

        if len(numbers) == 2:
            yield Constraint(cells, numbers)
        elif len(numbers) > 2:
            pass
