from ..solver.finder import Finder
from ..model.constraint import Constraint


class ConstraintFinder(Finder):
    def find(self, board):
        self.found = []

        for box in board.boxes:
            self.find_box_constraint(box)

        for cells, number in self.found:
            board.add_constraint(cells, number)

    def find_box_constraint(self, box):
        numbers = box.available_numbers

        for number in numbers:
            cells = box.possible_cells_with(number)
            if len(cells) == 2 and cells.is_aligned:
                self.found.append((cells, number))
