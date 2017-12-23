from ..solver.finder import Finder


class AlignedBoxesFinder(Finder):
    def __init__(self, extra=False):
        super(AlignedBoxesFinder, self).__init__()

        self.extra = extra

    def find(self, board):
        result = super(AlignedBoxesFinder, self).find(board)

        for number in range(1, 10):
            for boxes in board.box_rows + board.box_columns:
                cells = boxes.cells.which_has(number)
                if len(cells) != 2:
                    continue

                candidates = boxes.cells.empty_cells
                for cell in cells:
                    candidates -= cell.effective_cells

                if self.extra:
                    candidates = candidates.filter(lambda cell: cell.can_be(number))

                if len(candidates) == 1:
                    result.found(candidates[0], number)
                    break

        return result
