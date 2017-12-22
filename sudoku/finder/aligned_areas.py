from ..solver.finder import Finder


class AlignedAreasFinder(Finder):
    def find(self, board):
        result = super(AlignedAreasFinder, self).find(board)

        for number in range(1, 10):
            for areas in board.area_rows + board.area_columns:
                cells = areas.cells.which_has(number)
                if len(cells) != 2:
                    continue

                candidates = areas.cells.empty_cells
                for cell in cells:
                    candidates -= cell.effective_cells

                if len(candidates) == 1:
                    result.found(candidates[0], number)
                    break

        return result
